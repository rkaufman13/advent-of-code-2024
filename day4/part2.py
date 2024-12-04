from utils.open_and_read import open_and_read

path="full.txt"

data = open_and_read(path)

total_xmas = 0

for y in range(1,len(data)):
    for x in range(1, len(data[y])):
        try:
            if data[y][x]=='A':
                if (data[y-1][x-1] == 'M' and data[y+1][x+1]=='S') or (data[y-1][x-1] == 'S' and data[y+1][x+1]=='M'):
                    if (data[y-1][x+1] == 'M' and data[y+1][x-1]=='S') or (data[y-1][x+1] == 'S' and data[y+1][x-1]=='M'):
                        total_xmas+=1
        except IndexError:
            continue

print(total_xmas)