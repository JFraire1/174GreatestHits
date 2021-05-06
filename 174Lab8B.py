from itertools import islice

board = [" "," "," "],[" "," "," "],[" "," "," "]

num = 0

def turn(board,num):
    if num % 2 == 1:
        print("Player X Turn")
        i = (int(input("Enter a row number:")) - 1)
        j = (int(input("Enter a column number:")) - 1)
        board[i][j] = "X"

    elif num % 2 == 0:
        print("Player O Turn")
        i = (int(input("Enter a row number:")) - 1)
        j = (int(input("Enter a column number:")) - 1)
        board[i][j] = "O"

    return board


def printBoard(board):
    print("-------")      
    for i in range(len(board)):
        for j in range(len(board[i])):
            print("|" + board[i][j], end = '')
        print("|")
    print("-------")


def checkWinner(board):
    x_win = False
    o_win = False


    for i in range(len(board)):
        if board[i].count("X") == 3:
            return "x_win"
        elif board[i].count("O") == 3:
            return "o_win"


    columns = separateColumns(board)
    for i in range(len(columns)):
        if columns[i].count("X") == 3:
            return "x_win"
        elif columns[i].count("O") == 3:
            return "o_win"
            


    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return "x_win"
        elif board[0][0] == "O":
            return "o_win"

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return "x_win"
        elif board[0][2] == "O":
            return "o_win"

    if x_win == False and o_win == False:
        num = 0
        for i in range(len(board)):
            num += board[i].count(" ")


        if num == 0:
            return "tie"
        else:
            return"unfinished"
    

def separateColumns(board):
    columns = []
    divisions = [3,3,3]
    for k in range(len(board[0])):
        for i in range(len(board)):
            columns.append(board[i][k])
    column = iter(columns)
    columns = [list(islice(column,elem))
               for elem in divisions]
        
    return columns
            

def printWinner(result, num):
    if result == "x_win":
        printBoard(board)
        print("Player X is the winner")
    elif result == "o_win":
        printBoard(board)
        print("Player O is the winner")
    elif result == "tie":
        printBoard(board)
        print("It is a tie")
    elif result == "unfinished":
        main(board, num)


def main(board,num):
    num += 1
    printBoard(board)
    board = turn(board,num)
    printWinner(checkWinner(board),num)

main(board,num)
