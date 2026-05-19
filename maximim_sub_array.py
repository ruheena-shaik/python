#maximum sum sub array 19-5
numbers=[]
n=int(input("Enter number of elements: "))
i=0
while i<n:
    digi=int(input("Enter number: "))
    numbers = numbers + [digi]
    i=i+1
maximum = numbers[0]
sum=numbers[0]
i=1
while i<len(numbers):
    if sum+numbers[i] > numbers[i]:
        sum=sum+sum[i]
    else:
        sum = numbers[i]
    if sum > maximum:
        maximum = sum
    
    i=i+1
print("maximum sum sub array:",maximum)