#gcd 25-5

n = int(input("Enter the number: "))
m = int(input("Enter the number: "))
minimum = n

if m<n:
    minimum= m

i=minimum

while i>=1:

    if n % i == 0 and m % i == 0:
        print(i)
        break

    i=i-1