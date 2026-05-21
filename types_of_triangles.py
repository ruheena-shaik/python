# You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

# A triangle is called equilateral if it has all sides of equal length.
# A triangle is called isosceles if it has exactly two sides of equal length.
# A triangle is called scalene if all its sides are of different lengths.
# Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.
numbers=[]
for i in range(3):
    digi = int(input("Enter side: "))
    numbers=numbers+[digi]

side1=numbers[0]
side2=numbers[1]
side3=numbers[2]

if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
    print("none")

elif side1== side2 and side2== side3:
    print("equilateral")

elif side1 == side2 or side2 == side3 or side1 == side3:
    print("isosceles")
else:
    print("scalene")