#! /usr/bin/env python3
import sys
import random
import re

ERROR_MSG = "Not a valid dice notation."

def main(argv):
    random.seed()                         # generate a seed
    pattern = re.compile("[1-9]+d[1-9]+") # number d number 
    
    # parse the command line arguments
    for arg in argv:
        # ensure arg matches the pattern
        if(pattern.match(arg)):
            num = [ int(t) for t in arg.split('d')]

            for i in range(num[0]):
                print('{}'.format(random.randint(1,num[1])),end=" ")
            print()
        else:
            print(ERROR_MSG)
            return 1

    return 0


if __name__ == '__main__':
    main(sys.argv[1:])
