# Sudoku

b = []

print("Enter the Sudoku board (0 for empty cells):")
for i in range(9):
    row = [0,0,0,0,0,0,0,0,0]
    for j in range(9):
        row[j] = int(input())

    b = b + [row]

def solve():

    for i in range(9):
        for j in range(9):

            if b[i][j] == 0:

                for nums in range(1,10):
                    count = 0

                    for v in range(9):
                        if b[i][v] == nums:
                            count = count + 1

                    for v in range(9):
                        if b[v][j] == nums:
                            count = count + 1

                    vr = (i // 3) * 3
                    vc = (j // 3) * 3

                    for r in range(3):
                        for c in range(3):

                            if b[vr+r][vc+c] == nums:
                                count = count + 1
                    if count == 0:
                        b[i][j] = nums

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