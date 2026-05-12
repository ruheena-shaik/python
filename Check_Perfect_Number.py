# Check Perfect Number

# Check whether sum of factors equals the number.

# Ex 1: 6 → Perfect
# Ex 2: 8 → Not Perfect


n= int(input("Enter the number to check: "))

sum = 0
i = 1

while i < n:
    if n % i == 0:
        sum = sum + i
    i = i + 1
if sum == n:
    print("perfect number")
else:
    print("not perfect number")