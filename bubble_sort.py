# bubble sort 18-5
n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    digi = int(input("Enter number: "))
    numbers = numbers + [digi]
for i in range(n):
    for j in range(0, n-i-1):

        if numbers[j] > numbers[j + 1]:

            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
print("Sorted list:", numbers)