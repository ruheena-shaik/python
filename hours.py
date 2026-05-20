# There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked for hours[i] hours in the company.

# The company requires each employee to work for at least target hours.

# You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.

# Return the integer denoting the number of employees who worked at least target hours.

hours = []
n=int(input("Enter number of employees: "))

for i in range(n):

    digi = int(input("Enter working hours: "))
    hours = hours + [digi]
target = int(input("Enter target: "))

count = 0
for hour in hours:
    if hour >= target:
        count=count + 1
print(count)