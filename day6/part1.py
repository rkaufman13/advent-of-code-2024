from utils.open_and_read import open_and_read

path="sample.txt"

data = open_and_read(path)

x=0
y=0
for i in range(len(data)):
    data[i] = list(data[i].strip())
    if '^' in data[i]:
        y = i
        x = data[i].index('^')

directions = [(0,-1),(1,0),(0,1),(-1,0)]
visited=[]

def check_in_direction(direction,x,y):
    new_x = x+direction[0]
    new_y = y+direction[1]
    if not new_x>-1 and new_y>-1:
        raise IndexError("Guard went off the top or left of the page")
    if data[new_y][new_x]=="#":
        return False
    return True

def go_there(direction, x,y):
    new_x = x + direction[0]
    new_y = y + direction[1]
    visited.append((new_x,new_y))
    return new_x,new_y

def walk_maze(x,y):
    direction_index=0
    while True:
        try:
            direction=directions[direction_index]
            ahead_is_clear =check_in_direction(direction, x,y)
            if ahead_is_clear:
                x,y= go_there(direction, x,y)
            else:
                direction_index+=1
                if direction_index>3:
                    direction_index=0
        except IndexError:
            return

walk_maze(x,y)

print(len(set(visited)))

