#perfect number 25-5
#if the sum of the divisors is equal to the given number


n = int(input("Enter number: "))
total = 0
for i in range(1, n):
    if n % i == 0:
        total = total + i
    
if total==n:
    print("perfect number")
else:
    print("not a perfect number")