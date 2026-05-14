#sort the numbers(14-5)
numbers=[]
n=int(input("Enter the number of elements in the list;"))

for i in range(n):
    digi=int(input("Enter the number:"))
    numbers=numbers+[digi]

for i in range(n):

    for j in range(i+1,len(numbers)):
         
         if numbers[i]>numbers[j]:

            temp=numbers[i]
            numbers[i]=numbers[j]
            numbers[j]=temp

print("sorted list", numbers)

