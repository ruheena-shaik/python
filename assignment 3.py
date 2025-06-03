# factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

num = int(input("Enter a number: "))
print("Factorial of", num, "is:", factorial(num))

 #Square root of the number Natural logarithm (log base e) of the number  Sine of the number (in radians)

import math

num = float(input("Enter a number: "))

print("Square root:", math.sqrt(num))
print("Logarithm:", math.log(num))
print("Sine:", math.sin(num))
