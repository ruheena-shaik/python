#nu,ber to binary string

n= input("Enter the number:")
if n==0:
    print("0")
else:
    while n>0:
        binary=""
        remainder = n % 2
        binary = str(remainder) + binary
        n = n//2

    print(binary)