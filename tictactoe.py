#tic-tac-toe game
b=[]
print("Enter the game board  in X or O or _")

for i in range(3):

    row = [0, 0, 0]

    for j in range(3):
        row[j] = input()
    b=b+[row]

win= ""

for i in range(3):
    if b[i][0]==b[i][1] and b[i][1]==b[i][2]:
        if b[i][0]!= '_':
            win=b[i][0]

for i in range(3):
    if b[0][i]==b[1][i] and b[1][i]==b[2][i]:
        if b[0][i]!='_':
            win=b[0][i]

if b[0][0]==b[1][1] and b[1][1]==b[2][2]:
    if b[0][0]!='_':
        win=b[0][0]

if b[0][2]==b[1][1] and b[1][1]==b[2][0]:
    if b[0][2]!="_":
        win=b[0][2]

if win == 'X':
    print("X wins")

elif win=='O':
    print("O wins")


else:
    count = 0
    for i in range(3):
        for j in range(3):
            if b[i][j] == '_':
                count=count + 1
    if count>0:
        print("game in progress")

    else:
        print("draw")


