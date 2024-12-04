import re
import numpy as np

from utils.open_and_read import open_and_read

path="full.txt"

data = open_and_read(path)

total_xmas = 0


def find_horizontal(line):
    total=0
    r = 'XMAS'
    rr = 'SAMX' #two separate regex to allow for overlaps (:
    total+= len(re.findall(r,line))
    total+=len(re.findall(rr,line))
    return total

def find_vertical(numpy_array):
    total=0
    rotated = np.rot90(numpy_array)
    for line in rotated:
        total+= find_horizontal("".join(line))
    return total

#diagonals
def find_diagonal(numpy_array):
    start_of_range = len(numpy_array[0])-3
    end_of_range = start_of_range*-1
    total=0
    for i in range(end_of_range,start_of_range):
        diagonals_nw_to_se = np.diagonal(numpy_array, i)
        diagonals_ne_to_sw = np.diagonal(np.fliplr(numpy_array),i)
        total+=find_horizontal("".join(diagonals_nw_to_se))
        total+=find_horizontal("".join(diagonals_ne_to_sw))
    return total


for line in data:
    total_xmas+=find_horizontal(line)

numpy_array = data.copy()
for i in range(len(numpy_array)):
        numpy_array[i] = list(numpy_array[i].split()[0])
total_xmas+=find_vertical(numpy_array)
total_xmas+=find_diagonal(numpy_array)

print(total_xmas)
