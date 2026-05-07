# number to binary string and counting the number of 1's

n = int(input("Enter the number: "))
count = 0
binary = ""
if n == 0:
    print("Binary:", 0)
    print("number of 1's:", 0)
else:
    while n > 0:
        remainder = n % 2
        if remainder == 1:
            count = count + 1
        binary = str(remainder) + binary
        n = n // 2
    print("Binary:", binary)
    print("number of 1's:", count)