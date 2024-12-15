from utils.open_and_read import open_and_read
path="full.txt"
import tqdm

data = [int(num) for num in list(open_and_read(path)[0].strip().split())]

for i in tqdm.tqdm(range(25)):
    new_data = []
    for idx,num in enumerate(data):
        if num==0:
            new_data.append(1)
        elif len(str(num))%2==0:
            num1 = int(str(num)[0:len(str(num))//2])
            num2 = int(str(num)[len(str(num))//2:len(str(num))])
            new_data.append(num1)
            new_data.append(num2)
        else:
            new_data.append(num*2024)
    data = new_data
print(len(data))