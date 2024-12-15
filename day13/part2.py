
path="full.txt"

machines = []

machine = {}

machines_count=0

with open(path, 'r') as file:
    for line in file:
        if "Button A" in line:
            machines_count+=1
            processed = line.strip()[10:].split(",")
            obj = {"X":int(processed[0].split("+")[1]),"Y":int(processed[1].split("+")[1])}
            machine["A"] = obj
        elif "Button B" in line:
            processed = line.strip()[10:].split(",")
            obj = {"X":int(processed[0].split("+")[1]),"Y":int(processed[1].split("+")[1])}
            machine["B"]=obj
        elif "Prize" in line:
            processed=line.strip()[7:].split(",")
            obj={"X":int(processed[0].split("=")[1]),"Y":int(processed[1].split("=")[1])}
            machine["P"]=obj
        else:
            machines.append(machine)
            machine = {}

assert len(machines)==machines_count

spent = 0
for machine in machines:
    goal_x = machine["P"]["X"]
    goal_y = machine["P"]["Y"]
    a_x = machine["A"]["X"]
    a_y = machine["A"]["Y"]
    b_x = machine["B"]["X"]
    b_y=machine["B"]["Y"]

    #determine upper limit of button presses

    upper_limit_a_x = (goal_x//a_x)+1
    upper_limit_a_y = (goal_y//a_y)+1
    upper_limit_a = min(upper_limit_a_x,upper_limit_a_y)+1

    upper_limit_b = min((goal_x//b_x)+1,(goal_y//b_y))+1

  

    for i in range(100):
        for j in range(100):
            x = a_x*i+b_x*j
            y = a_y*i+b_y*j
            if x==goal_x and y==goal_y:
                spent+=(i*3)+j

print(spent)

#ans>22559
#ans>26597