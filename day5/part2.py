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

def sort_update(update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            index1 = update.index(rule[0])
            index2 = update.index(rule[1])
            if index2<index1:
                new_update = update.copy()
                item1 = rule[0]
                item2 = rule[1]
                new_update[index1] = item2
                new_update[index2] = item1
                update=new_update
    return update

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
   if not valid:
       valid_after_sorting = False
       sorted_update = update.copy()
       while not valid_after_sorting:
           sorted_update = sort_update(sorted_update)
           valid_after_sorting = validate_update(sorted_update)
       total+=  find_middle(sorted_update)

print(total)