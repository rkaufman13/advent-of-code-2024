from utils.open_and_read import open_and_read

path="full.txt"

data=open_and_read(path)



rules = []
updates = []
for line in data:
    if "|" in line:
        rules.append([int(page) for page in line.split()[0].split("|")])
    elif "," in line:
        updates.append([int(page) for page in line.split()[0].split(",")])

def validate_update(update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[1])<update.index(rule[0]):
                return False
    return True

def find_middle(update):
    return update[(len(update)-1)//2]

total = 0
for update in updates:
   valid= validate_update(update)
   if valid:
     total+=  find_middle(update)

print(total)