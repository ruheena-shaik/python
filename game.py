# Alice and Bob are playing a game. In the game, Alice can choose either all single-digit numbers or all double-digit numbers from nums, and the rest of the numbers are given to Bob. Alice wins if the sum of her numbers is strictly greater than the sum of Bob's numbers.

# Return true if Alice can win this game, otherwise, return false.

 
numbers = []

n = int(input("Enter number of elements: "))

for i in range(n):
    digi= int(input("Enter number: "))
    numbers = numbers + [digi]

single=0
double=0
total=0

for i in numbers:
    total=total + i
    if i <= 9:
        single=single+i

    elif i<=99:
        double = double+i

if single > total-single or double > total - double:
    print(True)
else:
    print(False)