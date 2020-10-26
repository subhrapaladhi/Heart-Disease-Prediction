# calculae the average age of people  who get and don't get heart disease
import sys
# input from STDIN
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    age = line[0]
    target = line[13]

    print("{}\t{}".format(target,age))