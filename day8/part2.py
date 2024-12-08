from utils.open_and_read import open_and_read
import itertools
import tqdm

import copy

path="full.txt"

data=open_and_read(path)

for idx, line in enumerate(data):
    data[idx] = list(line.strip())

def calculate_manhattan_distance(pair):
    point1 = pair[0]
    point2=pair[1]
    x = point1[0]-point2[0]
    y = point1[1]-point2[1]
    return x,y


def find_next(point, direction, diff):
    x = point[0]
    y = point[1]
    return x+diff[0]*direction, y+diff[1]*direction

antennas = {}
#first, get all unique types of antenna
for y,line in enumerate(data):
    for x,char in enumerate(line):
        if char !="." and char !="#":
            existing_coords = antennas.get(char,[])
            existing_coords.append((x,y))
            antennas.update({char:existing_coords})


list_of_possible_antinodes = []
writable_data = copy.deepcopy(data)

for antenna in tqdm.tqdm(antennas.keys()):

    list_of_positions = antennas[antenna]
    all_pairs = itertools.combinations(list_of_positions,2)
    direction = 1
    for pair in all_pairs:
        x_diff, y_diff = calculate_manhattan_distance(pair)
        for point in pair:
            for direction in [1,-1]:
                x,y = find_next(point, direction, (x_diff,y_diff))
                while 0 <= x < len(data[0]) and 0 <= y < len(data):
                    writable_data[y][x] = "#"
                    x,y = find_next((x,y), direction, (x_diff,y_diff))

print(len([ant for line in writable_data for ant in line if ant!="."]))