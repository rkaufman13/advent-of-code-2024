import numpy
from matplotlib import pyplot as plt
from utils.open_and_read import open_and_read
path="full.txt"

data=open_and_read(path)

robots = []

border_x = 101
border_y = 103

class Robot():
    def __init__(self, initial_pos, v_x,v_y):
        self.pos = initial_pos
        self.v_x = v_x
        self.v_y = v_y

    def __repr__(self):
        return f"Beep: position: {self.pos}: velocity: x: {self.v_x}, y: {self.v_y} "


    def get_pos(self):
        return self.pos

    def move(self):
        new_x = self.pos[0]+self.v_x
        new_y = self.pos[1]+self.v_y
        if new_x < 0:
            new_x = new_x+border_x
        elif new_x >=border_x:
            new_x = new_x-border_x
        if new_y <0:
            new_y = new_y+border_y
        elif new_y >=border_y:
            new_y = new_y-border_y
        self.pos=(new_x,new_y)

for line in data:
    coords = line.split()
    init_pos = coords[0].split("=")[1].split(",")
    velocity = coords[1].split("=")[1].split(",")
    robots.append(Robot((int(init_pos[0]),int(init_pos[1])),int(velocity[0]),int(velocity[1])))

grid = numpy.zeros(shape=(border_y,border_x))
count=499
iteration=0
while count<500:
    grid = numpy.zeros(shape=(border_y,border_x))
    for robot in robots:
        robot.move()
        pos = robot.get_pos()
        x = pos[0]
        y=pos[1]
        grid[y][x]=1
    count = numpy.sum(grid)
    iteration+=1
print(iteration)

plt.imshow(grid, interpolation='nearest')
plt.text(5,5,f"iteration: {iteration}", bbox={'facecolor': 'white', 'pad': 10})
plt.show()
