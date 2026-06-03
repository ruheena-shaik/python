#suduko puzzle test cases
b = []
print("Enter the puzzle:")
for i in range(9):
    row = [0,0,0,0,0,0,0,0,0]
    for j in range(9):
        row[j] = int(input())

    b = b+[row]

def valid():
#checks rows
#test case : sudoko with duplicates in row
    for i in range(9):

        for num in range(1,10):
            count = 0
            for j in range(9):
                if b[i][j] == num:
                    count += 1
            if count>1:
                return False
#checks columns
#test case: duplicates in column
    for j in range(9):

        for num in range(1,10):
            count=0
            for i in range(9):

                if b[i][j]==num:
                    count+=1
            if count>1:
                return False
#checks 3x3 boxes
#test case: duplicate numbers in box
    for vr in range(0,9,3):
        for vc in range(0,9,3):
            for num in range(1,10):
                count=0
                for r in range(3):
                    for c in range(3):
                        if b[vr+r][vc+c] == num:
                            count += 1
                if count > 1:
                    return False
    return True


def solve():

    for i in range(9):
        for j in range(9):
#test case: with empty cells
            if b[i][j] == 0:

#test case: one missing cell
#test case:multiple missing cell
#test case:all zero puzzl
                for num in range(1,10):
                    count=0

                    for v in range(9):
                        if b[i][v] == num:
                            count += 1

                    for v in range(9):

                        if b[v][j] == num:
                            count += 1

                    vr = (i//3) * 3
                    vc = (j//3) * 3

                    for r in range(3):
                        for c in range(3):
                            if b[vr+r][vc+c] == num:
                                count += 1

                    if count==0:
                        b[i][j] = num
                        if solve():
                            return True
                        #test case: wrong choice goes back again
                        b[i][j] = 0

                return False

    return valid()


if not valid():

    print("invalid Sudoku")

elif solve():

    print("solved Sudoku:")

    for i in range(9):
        for j in range(9):

            print(b[i][j], end=" ")

        print()
else:

    print("no solution exists")