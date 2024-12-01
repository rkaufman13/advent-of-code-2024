from collections import Counter
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

counts = Counter(list2)

for i in range(len(list1)):
    number = list1[i]
    total+= number * counts.get(number,0)

print(total)