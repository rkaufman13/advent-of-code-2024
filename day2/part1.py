from utils.open_and_read import open_and_read

path = "full.txt"


data = open_and_read(path)

parsed = []

for line in data:
    parsed.append([int(num) for num in line.split()])

def check_safety(line):
    if not line[0] < line[1]:
        line = line[::-1]
    for i in range(len(line)):
        try:
            if line[i] > line[i + 1] or line[i]==line[i+1] or line[i]+4<=line[i+1]:
                return False
        except IndexError:
            return True

safe = 0
for line in parsed:
   result = check_safety(line)
   if result:
       safe+=1

print(safe)