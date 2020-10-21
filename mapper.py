import sys
# input from STDIN
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    age = line[0]
    target = line[13]

    print("{}\t{}".format(target,age))