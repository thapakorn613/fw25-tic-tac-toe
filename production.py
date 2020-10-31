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
    print(" "*3 , end = "")
    for i in range(N):
        print((str(i)+ " "*(3))[:3], end = "")
    print()
    for row in range(N):
        print((str(row)+ " "*(3))[:3], end = "")
        for col in range(N):
            print(board[row][col], end = "    ")
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
#------------------------------------------

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
    n = len(board)
    temp = ""
    new_board = [[x for x in y] for y in board]
    
    # ! Check Case 1 all Row
    countCheckCase1 = 0
    for i in range(n):
        checkDrawCheck1 = []
        for j in range(n):
            checkDrawCheck1.append(new_board[i][j])
        if (findInList(checkDrawCheck1, "X") and findInList(checkDrawCheck1, "O")):
            countCheckCase1 += 1
        if (len(checkDrawCheck1) > 0 and all(elem == "X" for elem in checkDrawCheck1)):
            temp = "X"
            break
        elif (len(checkDrawCheck1) > 0 and all(elem == "O" for elem in checkDrawCheck1)):
            temp = "O"
            break
        else:
            temp = "-"
    if (temp == "O" or temp == "X"):
        return temp

    # ! Check Case 2 all Col
    countCheckCase2 = 0
    for i in range(n):
        checkDrawCheck2 = []
        for j in range(n):
            checkDrawCheck2.append(new_board[j][i])
        if (findInList(checkDrawCheck2, "X") and findInList(checkDrawCheck2, "O")):
            countCheckCase2 += 1
        if (len(checkDrawCheck2) > 0 and all(elem == "X" for elem in checkDrawCheck2)):
            temp = "X"
            break
        elif (len(checkDrawCheck2) > 0 and all(elem == "O" for elem in checkDrawCheck2)):
            temp = "O"
            break
        else:
            temp = "-"
    if (temp == "O" or temp == "X"):
        return temp

    # ! Check Case 3
    countCheckCase3 = 0
    checkDrawCheck3 = []
    for i in range(n):
        checkDrawCheck3.append(new_board[i][i])
    if (findInList(checkDrawCheck3, "X") and findInList(checkDrawCheck3, "O")):
        countCheckCase3 += 1
    if (len(checkDrawCheck3) > 0 and all(elem == "X" for elem in checkDrawCheck3)):
        print("X win")
        temp = "X"
    elif (len(checkDrawCheck3) > 0 and all(elem == "O" for elem in checkDrawCheck3)):
        temp = "O"
    else:
        temp = "-"
    if (temp == "O" or temp == "X"):
        return temp

    # ! Check Case 4
    countCheckCase4 = 0
    checkDrawCheck4 = []
    for i in range(n):
        checkDrawCheck4.append(new_board[i][n-(i+1)])
    if (findInList(checkDrawCheck4, "X") and findInList(checkDrawCheck4, "O")):
        countCheckCase4 += 1
    if (len(checkDrawCheck4) > 0 and all(elem == "X" for elem in checkDrawCheck4)):
        temp = "X"
    elif (len(checkDrawCheck4) > 0 and all(elem == "O" for elem in checkDrawCheck4)):
        temp = "O"
    else:
        temp = "-"

    # ? Check End Result
    if (countCheckCase1 >= n and countCheckCase2 >= n and countCheckCase3 >= 1 and countCheckCase4 >= 1):
        return "D"
    if (temp == "O" or temp == "X"):
        return temp
    return "-"




#------------------------------------------

main()