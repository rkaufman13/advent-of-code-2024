from utils.open_and_read import open_and_read
import tqdm
from collections import defaultdict

path="full.txt"

score =0
data = open_and_read(path)

for idx, line in enumerate(data):
    data[idx] = [int(num) for num in line.strip()]

mountain = {}
starting_pos = []

#get starting positions
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x]==0:
            starting_pos.append((x,y))

visited = {}

def get_room(coordinate):

        return data[coordinate[1]][coordinate[0]]

def validate_move(old,new):
    is_valid_by_size = -1<new[0]<len(data[0]) and -1<new[1]<len(data)
    if not is_valid_by_size:
        return False
    old_height = get_room(old)
    new_height = get_room(new)
    is_valid_by_height = old_height+1==new_height
   # is_not_visited = get_room(new,visited).get("visited")==False
    is_not_visited = True
    return is_valid_by_height and is_valid_by_size and is_not_visited

def walk_maze(coordinate):
    global score
    value = get_room(coordinate)

    #if room has value 9, append coordinates to our result list

    if value ==9:
        score+=1

    #choose a direction
    directions = [(0,-1),(1,0),(0,1),(-1,0)]
    valid_exits = []
    for direction in directions:
        new_coordinate = (coordinate[0]+direction[0],coordinate[1]+direction[1])
        is_valid = validate_move(coordinate,new_coordinate)
        if is_valid:
            valid_exits.append(new_coordinate)

    while len(valid_exits):
        new_coordinate = valid_exits.pop()
        #check that move is legal, both from a going-off-the-map perspective and from a value perspective
        is_valid = validate_move(coordinate,new_coordinate)
        #if so, go there by recursing
        if is_valid:
            walk_maze(new_coordinate)


final_score=0

for trailhead in starting_pos:
    walk_maze(trailhead)
    final_score+=score
    score=0
print(final_score)