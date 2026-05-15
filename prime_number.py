#prime number(15-5)
n=int(input("Enter the number: "))

count_divisible=0

for i in range(1,n+1):
    if n%i==0:
        count_divisible +=1

if count_divisible==2:
    print("prime")
else:
    print("not prime")
