# linear search 18-5
n = int(input("Enter number of elements: "))

numbers = []
for i in range(n):
    digi = int(input("Enter number: "))
    numbers = numbers + [digi]
number_to_find= int(input("Enter target number: "))

found = False
for i in range(len(numbers)):
    if numbers[i] == number_to_find:
        found = True
        print("target found at index", i)
if found == False:
    print("target not found")