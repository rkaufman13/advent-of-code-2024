
from utils.open_and_read import open_and_read

path = "full.txt"


data = open_and_read(path)

list1 = []
list2 = []
total=0
for line in data:
    line = line.split()
    list1.append(int(line[0]))
    list2.append(int(line[1]))

list1.sort()
list2.sort()
for i in range(len(list1)):
    total+= abs(list1[i]-list2[i])

print(total)