# Define two integers as follows:

# num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
# num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
# Return the integer num1 - num2.

n=int(input("Enter n: "))
m=int(input("Enter m: "))
number1=0
number2=0

for i in range (1,n+1):
    if i % m==0:
        number2=number2 + i
    
    else:
        number1=number1+i
result = number1-number2
print(result)
    



