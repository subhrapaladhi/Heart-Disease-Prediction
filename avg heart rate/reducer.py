import sys

def check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

avg_heartrate = {}

# Partitoner 
for line in sys.stdin:
    line = line.strip()
    target,heartRate = line.split("\t")

    if target in avg_heartrate:
        avg_heartrate[target].append(float(heartRate))
    else:
        if check(target):
            avg_heartrate[target] = []
            avg_heartrate[target].append(float(heartRate))

# Reducer
for target in avg_heartrate.keys():
    avg_age = sum(avg_heartrate[target])*1.0/len(avg_heartrate[target])
    print("target = {}\t avg maximum heart rate = {}".format(target,avg_age))