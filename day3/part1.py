import re
from utils.open_and_read import open_and_read

path="full.txt"


data = open_and_read(path)

regx="mul\(\d+,\d+\)"
num_regx = "\d+"
muls = []
for line in data:
    muls.append(re.findall(regx,line))

total =0
flat_muls = [
    x
    for xs in muls
    for x in xs
]

for mul in flat_muls:
    nums = re.findall(num_regx, mul)
    total+=int(nums[0])*int(nums[1])

print(total)