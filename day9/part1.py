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
        total+=int(idx)*int(value)
    return total



first_pass = []
for i in range(len(exploded)):
    working = exploded[i]
    first_pass.extend([working.get('id') for x in range (working.get('length'))])
    if working.get("allowed")<math.inf:
        first_pass.extend([None for x in range(working.get('allowed'))])

print(first_pass)
second_pass = []
i = 0

while i <len(first_pass):
    if first_pass[i] is not None:
        second_pass.append(first_pass[i])
        i+=1
    else:
        digit = None
        while not digit:
            digit = first_pass.pop(len(first_pass)-1)
        second_pass.append(digit)
        i+=1
print(second_pass)

checksum = find_checksum(second_pass[:-1])
print(checksum)
