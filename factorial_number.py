# factorial of a Number
n = int(input("Enter a number: "))

fact = 1
i = 1
while i <= n:
    fact = fact * i #multiplying the previous till the loop ends
    i += 1

print("factorial is:", fact)