n=int(input("Enter a Number: "))
size=len(str(n))
temp=n
arm=0
while temp>0:
    arm+=(temp%10)**size
    temp//=10
if n==arm:
    print("It is an Armstrong Number.")
else:
    print("It is NOT an Armstrong Number.")
