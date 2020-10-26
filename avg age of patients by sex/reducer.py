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

for sex in sex_age.keys():
    avg_age = sum(sex_age[sex])*1.0/len(sex_age[sex])
    print("sex = {}\t avg age = {}".format(sex,avg_age))