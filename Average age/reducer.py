import sys

def check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

target_age = {}

#Partitoner 

for line in sys.stdin:
    line = line.strip()
    target,age = line.split("\t")

    if target in target_age:
        target_age[target].append(float(age))
    else:
        if check(target):
            target_age[target] = []
            target_age[target].append(float(age))

# Reducer

for target in target_age.keys():
    avg_age = sum(target_age[target])*1.0/len(target_age[target])
    print("{}\t{}".format(target,avg_age))