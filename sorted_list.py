#sort the unsorted list of 0's/1's/2's
numbers = []   # creates empty list

n = int(input("Enter the number of elements in the list: "))
i = 0
while i < n:
    values = int(input("Enter the number 0/1/2 : "))
    numbers = numbers + [values]
    i += 1

# count number of 0s, 1s, 2s
count_zero = 0
count_one = 0
count_two = 0

i = 0
while i<len(numbers):

    if numbers[i] == 0:
        count_zero += 1

    elif numbers[i] == 1:
        count_one += 1

    elif numbers[i] == 2:
        count_two += 1
    i += 1
# updating list into sorted order
i = 0
#first print th lower like 0 next 1 and next 2 
while count_zero > 0:  
    numbers[i] = 0
    i += 1
    count_zero -= 1
while count_one > 0:
    numbers[i] = 1
    i += 1
    count_one -= 1
while count_two > 0:
    numbers[i] = 2
    i += 1
    count_two -= 1

print("sorted list:", numbers)