# Given an integer num, return the number of digits in num that divide num.

# An integer val divides nums if nums % val == 0.
numbers=int(input("Enter number: "))

temp=numbers
count=0
while temp>0:

    digit = temp % 10
    if numbers % digit == 0:
        count = count + 1

    temp = temp//10
print(count)