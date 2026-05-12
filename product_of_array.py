#Product of Array Except Self 
# Return array where each element is product of all other elements.
#  Ex 1: [1,2,3,4] → [24,12,8,6] Ex 2: [2,3] → [3,2]


nums = []

n = int(input("Enter size: "))
i = 0
while i < n:
    value = int(input("Enter number: "))
    nums = nums + [value]
    i = i + 1

result = []
i = 0
while i < len(nums):

    product = 1
    j = 0

    while j < len(nums):

        if i != j:
            product = product * nums[j]

        j = j + 1
    result = result + [product]
    i = i + 1
print(result)