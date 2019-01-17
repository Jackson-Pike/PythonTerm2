#Dominic Santistevan
#Tic Tac Toe

#Global Variables
x = "X"
o = "O"
empty = " "
tie = "TIE"
numSquares = 9

#Functions
def instructions():
    print("""These are the game instructions:

You will make you rmove known by entering a number, 0 - 8. The
number will correspond to the board posiiton as illustrated:


        0|1|2
        -----
        3|4|5
        -----
        6|7|8
\n
""")


def askYesNo(question):
    response = None
    while response not in ("y","n"):
        reponse = input(question+" y or n").lower()
    return response

def askNum(question, low, high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response = input("question")
        else:
            print("Enter a number")
            reponse = input(question)
    return int(response)

#x = askNumber("Enter a number between 1 and 10",1,11)
#print(x)

def pieces():
    goFirst = askYesNo("Will you go first? Yes or No?")
    if goFirst == ("y"):
        print("\nAdd in a taunt")
        human = x
        computer = o
    else:
        print("Add in a taunt")
        human = o
        computer = x
    return computer, human
#computer, human = pieces()
        
#print(computer)
#print(human)

def newBoard():
    board = []
    for squares in range (numSquares):
        board.append(empty)
    return board

board = newBoard()
#print(board)

def displayBoard():
    print("\n\t",board[0],"|",board[1],"|", board[2])
    print("\t","-----")
    print("\t",board[3],"|",board[4],"|", board[5])
    print("\t","-----",)
    print("\t",board[6],"|",board[7],"|", board[8],"\n")

#board = newBoard()
#displayBoard(board)

def legalMoves():
    moves = []
    for square in range(len(board)):
        if board[square] == empty:
            moves.append(square)
    return moves

#board = newBoard()
#moves = legalMoves(board)
#rint(moves)

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    
    for row in WAY_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner

        if empty not in board:
            return tie

        return None
            
board = [o,o,o,empty,empty,empty,empty,empty,empty]
win = winner(board)
print(win)


def computerTaunt():
    print("Not the best decision")
    print("")
def information():
    print()
def main():
    print("Welcome to TicTacToe")
    instructions()
    
