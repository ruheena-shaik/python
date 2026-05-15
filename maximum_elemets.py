#maximum elements(15-5)
numbers=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    digi=int(input("Enter the number:"))
    numbers=numbers+[digi]

maxi = numbers[0]
for i in range(1, len(numbers)):
    if numbers[i] > maxi:
        maxi = numbers[i]

print("maximum element is:", maxi)