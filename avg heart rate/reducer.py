import sys

def check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

target_heartrate = {}

# Partitoner 
for line in sys.stdin:
    line = line.strip()
    target,heartRate = line.split("\t")

    if target in target_heartrate:
        target_heartrate[target].append(float(heartRate))
    else:
        if check(target):
            target_heartrate[target] = []
            target_heartrate[target].append(float(heartRate))

# Reducer
for target in target_heartrate.keys():
    avg_heartrate = sum(target_heartrate[target])*1.0/len(target_heartrate[target])
    print("target = {}\t avg maximum heart rate = {}".format(target,avg_heartrate))