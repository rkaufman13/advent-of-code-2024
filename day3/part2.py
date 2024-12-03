import re
from utils.open_and_read import open_and_read

path="full.txt"


data = open_and_read(path)

regx="mul\(\d+,\d+\)"
num_regx = "\d+"
do_regx="do\(\)"
dont_regx="don't\(\)"
muls = []

def split_line_on_do_command(data):
    splits=[]
    continue_to_next_line = False
    for line in data:
        split_line = re.split(do_regx,line)
        if continue_to_next_line:
            split_line = split_line[1:]
        #special handling for end of line
        end_of_line = split_line[-1]
        if re.search(dont_regx,end_of_line):
            continue_to_next_line = True
        else:
            continue_to_next_line = False
        for split in split_line:
            splits.append(split)
    return splits

def split_on_dont_command(splits):
    splits_minus_donts=[]
    for split in splits:
        split_on_dont = re.split(dont_regx, split)
        splits_minus_donts.append(split_on_dont[0])
    return splits_minus_donts

splits =split_line_on_do_command(data)
splits_minus_donts = split_on_dont_command(splits)

for line in splits_minus_donts:
    results = re.findall(regx,line)
    for result in results:
        muls.append(result)

total =0


sample_2 = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
test_split = split_line_on_do_command(sample_2)
assert(len(test_split)==2)
assert(len(split_on_dont_command(test_split))==2)

for mul in muls:
    nums = re.findall(num_regx, mul)
    total+=int(nums[0])*int(nums[1])

print(total)

