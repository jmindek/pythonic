import sys

nums=[56,5,-92,3,11,213,41,23,41,1,93,2,54,-9,15,0]

def greatest2(nums):
    f=nums[1]
    s=nums[2]
    for num in nums:
        if num>f:
            s=f
            f=num
        elif num>s:
            s=num
    print "First {0} second {1}".format(f,s)

if __name__ == "__main__":
    sys.exit(greatest2(nums))
