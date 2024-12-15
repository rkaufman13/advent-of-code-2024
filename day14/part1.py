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

quadrants = {"NW":[],"NE":[],"SW":[],"SE":[]}

for robot in robots:
    for i in range(100):
        robot.move()
    pos = robot.get_pos()
    x = pos[0]
    y = pos[1]
    median_x = (border_x-1)//2
    median_y = (border_y-1)//2
    if x < median_x and y < median_y:
        nw = quadrants.get("NW")
        nw.append(robot)
        quadrants["NW"]=nw
    elif x >median_x and y <median_y:
        ne = quadrants.get("NE")
        ne.append(robot)
        quadrants["NE"] = ne
    elif x > median_x and y >median_y:
        se = quadrants.get("SE")
        se.append(robot)
        quadrants["SE"] = se
    elif x < median_x and y > median_y:
        sw = quadrants.get("SW")
        sw.append(robot)
        quadrants["SW"]=sw

print(len(quadrants.get("NW"))*len(quadrants.get("NE"))*len(quadrants.get("SE"))*len(quadrants.get("SW")))
