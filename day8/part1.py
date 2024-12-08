from utils.open_and_read import open_and_read
import itertools
import tqdm

path="full.txt"

data=open_and_read(path)

for idx, line in enumerate(data):
    data[idx] = list(line.strip())

def calculate_manhattan_distance(pair):
    point1 = pair[0]
    point2=pair[1]
    x = point1[0]-point2[0]
    y = point1[1]-point2[1]
    distance=abs(max(point1[0],point2[0])-min(point1[0],point2[0]))+abs(max(point1[1],point2[1])-min(point1[1],point2[1]))
    return x,y, distance


antennas = {}
#first, get all unique types of antenna
for y,line in enumerate(data):
    for x,char in enumerate(line):
        if char !="." and char !="#":
            existing_coords = antennas.get(char,[])
            existing_coords.append((x,y))
            antennas.update({char:existing_coords})


list_of_possible_antinodes = []

for antenna in tqdm.tqdm(antennas.keys()):

    list_of_positions = antennas[antenna]
    all_pairs = itertools.combinations(list_of_positions,2)
    for pair in all_pairs:
        x,y, distance = calculate_manhattan_distance(pair)
        antinode_1 = (pair[0][0]+x,pair[0][1]+y)
        antinode_2 = (pair[1][0]-x,pair[1][1]-y)
        antinode_1_x = antinode_1[0]
        antinode_1_y = antinode_1[1]
        antinode_2_x = antinode_2[0]
        antinode_2_y = antinode_2[1]
        if 0<= antinode_1_x<len(data[0]) and 0<=antinode_1_y<len(data):
            _,_,distance1 = calculate_manhattan_distance((antinode_1,pair[0]))
            _,_,distance2 = calculate_manhattan_distance((antinode_1,pair[1]))
            if not distance == distance1 or distance ==distance2:
                print("huh that's weird")
            list_of_possible_antinodes.append(antinode_1)

        if 0<= antinode_2_x<len(data[0]) and 0<=antinode_2_y<len(data):
            list_of_possible_antinodes.append(antinode_2)

#290<ans<319
print(len(set(list_of_possible_antinodes)))