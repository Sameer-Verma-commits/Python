import math
num=int(input("Enter a Number: "))
if num<2:
    print("It is NOT a Prime Number.")
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i==0:
            print("It is NOT a Prime Number.")
            break
    else:
        print("It is a Prime Number.")
