from utils.open_and_read import open_and_read
from itertools import pairwise, permutations
path = "full.txt"


data = open_and_read(path)

parsed = []

for line in data:
    parsed.append([int(num) for num in line.split()])

def check_safety(line, depth):
    differences = [second-first for first,second in pairwise(line)]
    invalid = [diff for diff in differences if diff <1 or diff >3]
    if all(0 > diff > -4 for diff in differences):
        invalid = []
    if depth==0:
        if len(invalid)==0:
            return True
        else:
            is_valid = False

            for idx, _ in enumerate(line):
                new_line = line[0:idx]+line[idx+1:len(line)]
                result = check_safety(new_line, depth+1)
                if result:
                    is_valid=True
            return is_valid
    if depth==1:
        return len(invalid)==0


bad_1 = [83, 82, 86, 87, 86]
good_1 = [48,46,47,49,51,54,56]
good_2 =  [64, 67, 69, 70, 74]

assert(check_safety(bad_1,0)==False)
assert(check_safety(good_1,0)==True)
assert(check_safety(good_2,0)==True)


safe = 0
for line in parsed:
   result = check_safety(line,0)
   if result:
       safe+=1

print(safe)