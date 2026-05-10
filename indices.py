nums = []
n=int(input("Enter the number of elements:"))
i=0
while i < n:
    value = int(input("Enter the number: "))
    nums = nums + [value]
    i=i+1
target  = int(input("Enter the value of the target"))

i= 0
while i < len(nums):
    j = i + 1
    while j < len(nums):
        if nums[i] + nums[j] == target:
            print("Indices are:", i, j)
        j = j + 1

    i = i + 1