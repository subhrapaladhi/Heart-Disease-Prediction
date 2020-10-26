import sys

def check(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

sex_age = {}

#Partitoner 

for line in sys.stdin:
    line = line.strip()
    sex,age = line.split("\t")

    if sex in sex_age:
        sex_age[sex].append(float(age))
    else:
        if check(sex):
            sex_age[sex] = []
            sex_age[sex].append(float(age))

# Reducer

for target in sex_age.keys():
    avg_age = sum(sex_age[target])*1.0/len(sex_age[target])
    print("{}\t{}".format(target,avg_age))