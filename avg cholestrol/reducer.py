import sys

def check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

target_cholestrol = {}

# Partitoner 
for line in sys.stdin:
    line = line.strip()
    target,cholestrol = line.split("\t")

    if target in target_cholestrol:
        target_cholestrol[target].append(float(cholestrol))
    else:
        if check(target):
            target_cholestrol[target] = []
            target_cholestrol[target].append(float(cholestrol))

# Reducer
for target in target_cholestrol.keys():
    avg_cholestrol = sum(target_cholestrol[target])*1.0/len(target_cholestrol[target])
    print("target = {}\t avg maximum cholestrol = {}".format(target,avg_cholestrol))