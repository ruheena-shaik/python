#check the list issorted or not(14-5)

numbers=[]
n=int(input("Enter the number of elements in the list: "))

for i in range(n):
    digi=int(input("Enter the number:"))
    numbers=numbers+[digi]

last=len(numbers)-1

for i in range(last):
    if numbers[i]>numbers[i+1]:
        flag = 0
    else:
        flag=1

if flag==1:
    print("sorted")
else:
    print("not sorted")

