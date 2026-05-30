# Sudoku puzzlw
b = []
print("Enter the puzzle:")
for i in range(9):
    row = [0,0,0,0,0,0,0,0,0]
    for j in range(9):
        row[j] = int(input())
    b=b+[row]

def solve():
    for i in range(9):
        for j in range(9):
            if b[i][j] == 0:

                for nums in range(1,10):
                    count = 0
#row
                    for v in range(9):
                        if b[i][v] == nums:
                            count = count + 1
#column
                    for v in range(9):
                        if b[v][j] == nums:
                            count = count + 1
#3X3 matrix
                    vr = (i // 3) * 3
                    vc = (j // 3) * 3

                    for r in range(3):
                        for c in range(3):

                            if b[vr+r][vc+c] == nums:
                                count = count + 1
                    if count == 0:
                        b[i][j] = nums
#again check
                        if solve():
                            return True
                        b[i][j] = 0
                return False
    return True

solve()
print("solved puzzle:")

for i in range(9):
    for j in range(9):
        print(b[i][j], end=" ")
    print()