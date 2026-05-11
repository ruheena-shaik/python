#jewles and stones
jewels = input("Enter jewels: ")
stones = input("Enter stones: ")
count = 0
i = 0
while i < len(stones):

    if stones[i] in jewels:
        count = count + 1
    i = i + 1

print("Number of jewel stones:", count)