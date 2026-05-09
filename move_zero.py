# Move all 0s to the end
n = int(input("Enter number of elements: "))

nums = []
for i in range(n):
    value = int(input("Enter element: "))
    nums = nums + [value]

result = []
for i in nums:
    if i != 0:
        result = result + [i]

count = len(nums) - len(result)

# add zeros at the end
for i in range(count):
    result = result + [0]

print("New list:", result)