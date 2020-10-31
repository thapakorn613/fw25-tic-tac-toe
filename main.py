# Prog-10: Tic-Tac-Toe
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

import random


def main():
    N = int(input('Board size = '))
    board = [["-"]*N for j in range(N)]
    end = False
    print_board(board)

    while(not end):
        print("========== Player Turn ==========")
        player_input(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("\\(^o^)/     YOU WIN !!!     \\(^o^)/")
            break
        print("======== Computer Turn ==========")
        com_fill(board)
        print_board(board)
        check = check_win(board)
        if(check != "-"):
            if(check == "D"):
                print("############# DRAW ##############")
            else:
                print("(;-;)    YOU LOSE!!!    (;-;)")
            break
    print("Game has ended, thanks for playing :D")


def com_fill(board):
    N = len(board)
    new_board = [[x for x in y] for y in board]
    for i in range(N):
        for j in range(N):
            if board[i][j] == "-":
                new_board[i][j] = "O"
                if(check_win(new_board) == "O"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "X"
                if(check_win(new_board) == "X"):
                    board[i][j] = "O"
                    return
                new_board[i][j] = "-"
    while True:
        i = random.randint(0, N-1)
        j = random.randint(0, N-1)
        if board[i][j] == "-":
            board[i][j] = "O"
            break


def print_board(board):
    N = len(board)
    print(" "*3, end="")
    for i in range(N):
        print((str(i) + " "*(3))[:3], end="")
    print()
    for row in range(N):
        print((str(row) + " "*(3))[:3], end="")
        for col in range(N):
            print(board[row][col], end="    ")
        print()


def player_input(board):
    f = False
    while not f:
        try:
            row = int(input("row = "))
            col = int(input("col = "))
            f = fill(board, row, col)
            if (not f):
                print("!!! You can't fill that spot !!!")
                print("---try again---")
        except:
            print("!!! Invalid Input !!!")
            print("---try again---")
# ------------------------------------------
def findInList(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def fill(board, r, c):
    if (board[r][c] == "-"):
        board[r][c] = "X"
        return True
    else:
        return False


def check_win(board):
    # N = len(board)
    n = 3 
    temp = ""
    # checkDraw = [False,False,False,False]
    new_board = [[x for x in y] for y in board]
    # print("baord: ",board)
    amountX = 0
    amountO = 0
    for i in range(3):
        for j in range(3):
            if(new_board[i][j] =="X"):
                amountX += 1
            elif(new_board[i][j] =="O"):
                amountO += 1
    # ! Check Case 1 all Row 
    countCheckCase1 = 0
    for i in range(3):
        x = new_board[i][0]
        y = new_board[i][1]
        z = new_board[i][2]
        tempCheckDraw = []
        tempCheckDraw.append(x)
        tempCheckDraw.append(y)
        tempCheckDraw.append(z)
        if ( findInList(tempCheckDraw,"X") and findInList(tempCheckDraw,"O") ):
            countCheckCase1 += 1
        if (x is y is z == "X"):
            print("X win")
            temp = "X"
            break
        elif (x is y is z == "O"):
            print("O win")
            temp = "O"
            break
        
            # temp = "D"
            # break
        else:
            temp = "-"
    
    if (temp == "O" or temp == "X"):
        return temp

    # ! Check Case 2 all Col
    countCheckCase2 = 0
    for i in range(3):
        x = new_board[0][i]
        y = new_board[1][i]
        z = new_board[2][i]
        tempCheckDraw = []
        tempCheckDraw.append(x)
        tempCheckDraw.append(y)
        tempCheckDraw.append(z)
        if ( findInList(tempCheckDraw,"X") and findInList(tempCheckDraw,"O") ):
            countCheckCase2 += 1
        if (x is y is z == "X"):
            print("X win")
            temp = "X"
            break
        elif (x is y is z == "O"):
            print("O win")
            temp = "O"
            break
        else:
            temp = "-"
    if (temp == "O" or temp == "X"):
        return temp
    
    # ! Check Case 3
    countCheckCase3 = 0
    x = new_board[0][0]
    y = new_board[1][1]
    z = new_board[2][2]
    checkDrawCheck3 = []
    checkDrawCheck3.append(x)
    checkDrawCheck3.append(y)
    checkDrawCheck3.append(z)
    if ( findInList(checkDrawCheck3,"X") and findInList(checkDrawCheck3,"O") ):
        countCheckCase3 += 1
    if (x is y is z == "X"):
        print("X win")
        temp = "X"
    elif (x is y is z == "O"):
        print("O win")
        temp = "O"
    else:
        temp = "-"
    if (temp == "O" or temp == "X"):
        return temp
    
    # ! Check Case 4
    countCheckCase4 = 0
    x = new_board[0][2]
    y = new_board[1][1]
    z = new_board[2][0]
    checkDrawCheck4 = []
    checkDrawCheck4.append(x)
    checkDrawCheck4.append(y)
    checkDrawCheck4.append(z)
    if ( findInList(checkDrawCheck4,"X") and findInList(checkDrawCheck4,"O") ):
        countCheckCase4 += 1
    if (x is y is z == "X"):
        print("X win")
        temp = "X"
    elif (x is y is z == "O"):
        print("O win")
        temp = "O"
    else:
        temp = "-"
    
    # ? Check End Result
    # if (amountO + amountX >= n*n):
    #     return "D"
    if (countCheckCase1 >= n and countCheckCase2 >= n and countCheckCase3 >=1 and countCheckCase4 >=1 ):
        return "D"
    if (temp == "O" or temp == "X"):
        return temp
    
    return "-"


# ------------------------------------------
main()
