import copy
import itertools
from tqdm import tqdm
from utils.open_and_read import open_and_read

path="sample.txt"

data = open_and_read(path)

for idx, line in enumerate(data):
    data[idx] = list(line.strip())

directions = [(0,-1),(1,0),(0,1),(-1,0)]

list_of_positions ={}
score = 0
group = 0

def get_spot(point):
    return list_of_positions.get(point,{})


def find_neighbors(point):
    neighbors=[]
    for direction in directions:
        new_point = (point[0]+direction[0],point[1]+direction[1])
        if -1<new_point[0]<len(data[0]) and -1<new_point[1]<len(data[1]):

            val = data[point[1]][point[0]]
            new_val = data[new_point[1]][new_point[0]]
            if  val==new_val:
                neighbors.append(new_point)
    walls=4-len(neighbors)
    return neighbors, walls

def walk_garden(point, depth):
    global score
    global group
    #first,check if visited
    visited = get_spot(point).get('visited')
    if visited:
        return
    #otherwise, find its neighbors and see how far the plot goes
    neighbors, walls = find_neighbors(point)
    point_dict = {'walls': walls, 'neighbors':neighbors, 'visited':True, 'group':group}
    list_of_positions[point]= point_dict
    for position in neighbors:
        walk_garden(position, depth+1)

    if depth==0:
        group+=1
#        score += calculate_area_and_perimeter(point)

for y in range(len(data)):
    for x in range(len(data[0])):
        walk_garden((x,y),0)

print(list_of_positions)

groups = [group for group in list_of_positions.values()]

sorted_groups = itertools.groupby(groups, key=lambda x:x['group'])


for key, batch in tqdm(sorted_groups):
    second_batch = copy.deepcopy(batch)
    area = len(list(second_batch))
    perimiter = sum(square.get('walls') for square in batch)
    score+=area*perimiter

print(score)
