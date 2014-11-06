nums=range(1,100)

for num in nums:
    if num%5==0 and num%3==0:
        print("Fizzbuzz")
    elif num%5==0:
        print("Buzz")
    elif num%3==0:
        print("Fizz")
    else:
        print num

