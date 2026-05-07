#binary string to number
s = input("Enter the binary string: ")
decimal = 0

i = 0
while i<len(s):
    decimal = decimal * 2 + int(s[i])

    i = i + 1
print(decimal)