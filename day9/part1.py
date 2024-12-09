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
                'value': i//2,
                'length': int(data[i]),
                'allowed': int(data[i+1]),
                'followed_by':[]
            })
    except IndexError:
        exploded.append({'value':i//2, 'length':int(data[i]),'allowed':math.inf})

formatted=[]

def find_checksum(string):
    total=0
    for idx,value in enumerate(string):
        total+=int(idx)*int(value)
    return total


def move_blocks(exploded, num_of_blocks, value):
    for i in range(num_of_blocks):
        total_added = 0
        while len(exploded):
            first = exploded.pop(0)
            blocks = first.get('followed_by')
            allowed = first.get('allowed')
            while len(blocks)<allowed:
                blocks.append(value)
                first['followed_by'] = blocks
                total_added += 1
                if len(blocks)==allowed:
                    # this sector is completely full
                    formatted.append(first)

                if total_added == num_of_blocks:
                    exploded = [first] + exploded
                    return exploded

try:
    while len(exploded)>1:
        last = exploded.pop()
        value = last.get('value')
        num_of_blocks = last.get('length')
        exploded = move_blocks(exploded, num_of_blocks, value)
except TypeError:
    remainder = last.get('value')
    blocks = last.get('followed_by')
    followed = [followed.get('followed_by') for followed in formatted]
    flat_followed = [num for nums in followed for num in nums ]
    remaining_blocks = last.get('length') - flat_followed.count(remainder)
    for i in range(remaining_blocks):
        blocks.append(remainder)
        last['followed_by'] = blocks
        last['length']=remaining_blocks-1 #hmm i don't know why this is here
        formatted.append(last)

    final = formatted
    if exploded:
        final = formatted+exploded
    print(final)
final_string = ""

for item in final:
        final_string+=str(item.get('value'))*item.get('length')
        final_string+="".join([str(num) for num in item.get('followed_by')])
print(final_string)

checksum = find_checksum(final_string)
print(checksum)
