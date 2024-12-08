import copy

import tqdm

from utils.open_and_read import open_and_read

class LoopError(Exception):
    #it's not an error, it means the guard has gotten stuck!
    pass

path="full.txt"

data = open_and_read(path)

start_x=0
start_y=0
for i in range(len(data)):
    data[i] = list(data[i].strip())
    if '^' in data[i]:
        start_y = i
        start_x = data[i].index('^')

directions = [(0,-1),(1,0),(0,1),(-1,0)]

def get_glyph(direction):
    match(direction):
        case (0,-1):
            return "^"
        case (1,0):
            return ">"
        case (0,1):
            return "v"
        case (-1,0):
            return "<"

def check_in_direction(maze, direction,x,y):
    new_x = x+direction[0]
    new_y = y+direction[1]
    if not new_x>-1 and new_y>-1:
        raise IndexError("Guard went off the top or left of the page")
    if maze[new_y][new_x]=="#":
        return False
    return True

def go_there(visited,direction, x,y):
    new_x = x + direction[0]
    new_y = y + direction[1]
    exits = visited.get((x,y),[])
    if (new_x,new_y) in exits:
        raise LoopError
    exits.append((new_x,new_y))
    visited.update({(x,y):exits})
    return new_x,new_y

def initial_walk(maze, x,y):
    direction_index = 0
    visited = {}
    while True:
        try:
            direction = directions[direction_index]
            ahead_is_clear = check_in_direction(maze, direction, x, y)
            if ahead_is_clear:
                x, y = go_there(visited, direction, x, y)
            else:
                direction_index += 1
                if direction_index > 3:
                    direction_index = 0
        except IndexError:
            visited.update({(x,y):None})
            return visited.keys()

def walk_maze(maze, x,y):
    direction_index=0
    visited={}
    while True:
        try:
            direction=directions[direction_index]
            maze[y][x] = get_glyph(direction)
            ahead_is_clear =check_in_direction(maze, direction, x,y)
            if ahead_is_clear:
                x,y= go_there(visited, direction, x,y)
            else:
                direction_index+=1
                if direction_index>3:
                    direction_index=0
        except IndexError:
            return False
        except LoopError:
            # for line in maze:
            #     print("".join(line))
            return True

points = set(initial_walk(data, start_x, start_y))


paradox_spots =[]
for x,y in tqdm.tqdm(points):
        new_data = copy.deepcopy(data)
        new_data[y][x]= "#"
        causes_infinite_loop = walk_maze(new_data, start_x,start_y)
        if causes_infinite_loop:
            paradox_spots.append((x,y))

if (start_x,start_y) in paradox_spots:
    paradox_spots.pop()
print(len(set(paradox_spots)))
