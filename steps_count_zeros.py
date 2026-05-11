#steps to count the zeros
n = int(input("Enter number: "))

steps = 0

while n > 0:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n - 1
    steps = steps + 1

print("Steps:", steps)