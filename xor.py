# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

numbers=[]
n=int(input("Enter the number:"))

st=int(input("Enter the start element:"))


for i in range(n):
    digi= st+2*i
    numbers= numbers + [digi]
xor_oper = 0
for i in range(n):
    xor_oper = xor_oper + numbers[i]

print("XOR",xor_oper)
