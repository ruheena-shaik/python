#the given number is even or odd
a=int(input("Enter a number: "))
if a % 2 ==0:
    print(a," is an even number")
else:
    print(a,"is an odd number")
############################################################
#loop and add
b = int(input("Enter a number: "))
sum = 0
for i in range(0, b + 1):
    sum = sum + i

print(sum)
