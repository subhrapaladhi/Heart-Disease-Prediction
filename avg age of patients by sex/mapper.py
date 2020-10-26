# target: 0-no 1-yes
import sys
# input from STDIN
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    # female = 0, male = 1
    age = line[0]
    sex = line[1]
    target = line[13]
    if(target==1):
        print("{}\t{}".format(sex,age))