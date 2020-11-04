# calculae the average age of people  who get and don't get heart disease
import sys
# input from STDIN
for line in sys.stdin:
    line = line.strip()
    line = line.split(",")
    
    cholestrol = line[4]
    target = line[13]

    print("{}\t{}".format(target,cholestrol))