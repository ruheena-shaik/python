# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

# Example 1:

# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
arr=[]
n = int(input("Enter number of elements: "))

for i in range(n):
    digi = int(input("Enter number: "))
    arr = arr + [digi]
count=0

for i in range(len(arr)):
    if arr[i] % 2 != 0:
        count = count + 1
    else:
        count = 0
    if count==3:
        print(True)
        break
else:
    print(False)