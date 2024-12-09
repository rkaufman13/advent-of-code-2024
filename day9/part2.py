import copy
import tqdm
from utils.open_and_read import open_and_read
import math
path="full.txt"

data=list(open_and_read(path)[0].strip())

exploded = []
for i in range(len(data)):
    try:
        if i %2 ==0:
            #file
            exploded.append({
                'id': i//2,
                'length': int(data[i]),
                'allowed': int(data[i+1]),
                'followed_by':[]
            })
    except IndexError:
        exploded.append({'id':i//2, 'length':int(data[i]),'allowed':math.inf})


def find_checksum(string):
    total=0
    for idx,value in enumerate(string):
        try:
            total+=int(idx)*int(value)
        except ValueError:
            pass
    return total



first_pass = []
for i in range(len(exploded)):
    working = exploded[i]
    first_pass.extend([working.get('id') for x in range (working.get('length'))])
    if working.get("allowed")<math.inf:
        first_pass.extend([None for x in range(working.get('allowed'))])

print(first_pass)

def find_valid_spot(len_to_find, pos, max):
    for i in range(pos,max):
        if first_pass[i] is None:
            length_of_none = find_length_of_block_from_start(i,None)
            if length_of_none>=len_to_find:
                return i
    return None

def find_length_of_block_from_start(pos, value):
    length=1

    for i in range(pos+1,len(first_pass)-1):
        if first_pass[i]==value:
            length+=1
        else:
            return length
    return 0

def find_length_of_block_from_end(pos, value):
    length=1

    for i in range(pos-1,0,-1):
        if first_pass[i]==value:
            length+=1
        else:
            return length

i = 0
j = len(first_pass)-1
#second_pass = [None for x in range(j)]
while i<len(first_pass) and i <j:
    if first_pass[i] is not None:
        length = find_length_of_block_from_start(i, first_pass[i])
        first_pass[i:i+length]=[first_pass[i]]*length
        i=i+length
    else:
        from_end = first_pass[j]
        while from_end is None:
            j -=1
            from_end=first_pass[j]
        length = find_length_of_block_from_end(j, from_end)
        spot = find_valid_spot(length, i,j)
        if spot:
            first_pass[spot:spot+length]=[from_end]*length
            if length>1:
                first_pass[j-(length-1):j+1]= [None]*length
            else:
                first_pass[j] = None
        j-=length


first_pass = [str(item) if item is not None else "." for item in first_pass ]
print("".join(first_pass))
checksum = find_checksum(first_pass)
print(checksum)
