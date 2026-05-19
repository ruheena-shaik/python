#binary search 18-5
numbers =[]
n= int(input("Enter number of elements: "))
i=0
while i<n:
    digi=int(input("Enter number in sorted order:"))
    numbers = numbers+[digi]
    i=i+1
target = int(input("Enter the elemet to find: "))
l = 0
r= len(numbers)-1
found = False

while l<r:
    middle= (l+r)//2

    if numbers[middle] == target:
        print("Element found at index: ",middle)
        found = True
        break
    elif numbers[middle]<target:
        l = middle +1
    else:
        r=middle -1
if found== False:
    print("Enter not found")