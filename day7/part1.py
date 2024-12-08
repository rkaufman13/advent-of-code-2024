from utils.open_and_read import open_and_read
import itertools
from functools import reduce
import tqdm


path="full.txt"

data = open_and_read(path)

equations=[]

def calculate_result(wanted, inputs, num_of_ops):
    perms = itertools.product(["*", "+",""],repeat=num_of_ops)
    for perm in perms:
            try:
                result=eval(inputs[0]+perm[0] + inputs[1])
                for i in range(1,len(inputs)+1):
                    new_str = str(result)+perm[i]+inputs[i+1]
                    result=eval(new_str)
                    if result>=wanted:
                        continue
            except IndexError:
                if result==wanted:
                    return result
    return 0


for index, line in enumerate(data):
    wanted = int(line.split(":")[0])
    inputs = line.split(":")[1].split()
    equations.append({"wanted":wanted, "inputs":inputs})

score =0
for equation in tqdm.tqdm(equations):
    wanted = equation.get("wanted")
    inputs = equation.get("inputs")
    num_of_ops = (len(inputs)-1)

    score += calculate_result(wanted, inputs, num_of_ops)
print(score)