# search in 2d matrix 18-5
r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
for i in range(r):
    row=[]
    for j in range(c):
        digi = int(input("Enter number: "))
        row = row + [digi]
    matrix=matrix+[row]
target = int(input("Enter target number: "))
found = False

for i in range(r):
    for j in range(c):
        if matrix[i][j] == target:
            found = True
if found == True:
    print("target found")

else:
    print("target not found")
    