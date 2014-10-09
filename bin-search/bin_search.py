import sys

sorted=[1,2,3,4,5,9,19,32,40,41]
findval=19

def bin_search(list):
    """Simple albeit ugly binary search algo"""
    if list:
        midpoint=len(list)/2
        mp_value=list[midpoint]

        if mp_value == findval:
            print "found {0}".format(findval)
            return
        elif findval < mp_value:
            bin_search(list[:midpoint])
        else:
            bin_search(list[midpoint+1:])
    else:
        print "didnt find {0}".format(findval)
        

if __name__ == "__main__":
    sys.exit(bin_search(sorted))

