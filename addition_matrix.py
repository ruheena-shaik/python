#addition of matrix(15-5)
r = int(input("Enter the number of elements in the row:"))
c= int(input("Enter the number of elements in the column:"))

matrix=[]

for i in range(r):
    ele=[]
    for j in range(c):
        digi=int(input("Enter the numbers:"))
        ele=ele+[digi]
    matrix = matrix+[ele]

total = 0
for i in range(r):
    for j in range(c):
        total=total + matrix[i][j]
print("sum of elements:", total)


              