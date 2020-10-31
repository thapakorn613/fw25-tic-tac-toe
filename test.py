# Prog-10: Tic-Tac-Toe
# Fill in your ID & Name
# ...
# Declare that you do this by yourself

import random


def main():
    # a = ["X", "O", "A"]
    # n = len(a)
    
    # for i in range(n)s:
    # ? print(a[(n-n):], a[(n-2):], a[(n-1):])
    # ? ziplist = zip( [ a[(n-(n-i)):] for i in range(n)] )
    # for i in range(n):
    #     # print(a[(n-(n-i)):])
    #     temp.append(a[(n-(n-i)):])
    # print(temp)
    # zip( [ print(a[(n-(n-i)):]) for i in range(n)] )

    # for x, y, z in zip( [ a[(n-(n-i)):] for i in range(n)] ):
    #     if (x is y is z == "X"):
    #         print("X win")
    #     else:
    #         print("O win")
    # for i in range(n):
    # print( [ a[(n-(n-i)):] for i in range(n)] )
    # for x, y, z in zip(a, a[(n-2):], a[(n-1):]):
    #     if (x is y is z == "X"):
    #         print("X win")
    #     else:
    #         print("O win")
    a = [
        ["O", "O", "-"],
        ["X", "X", "X"],
        ["-", "O", "-"]
    ]
    n = 3
    for i in range(n):
        x = a[i][0]
        y = a[i][1]
        z = a[i][2]
        if (x is y is z == "X"):
            print("X win")
        elif (x is y is z == "O"):
            print("O win")
        else:
            print("- win")

    # for i in range(len(a)-1):
    #     x = a[i]
    #     y = a[i+1]
    #     z = a[i+2]
    #     print (x,y,z)


# ------------------------------------------
main()
