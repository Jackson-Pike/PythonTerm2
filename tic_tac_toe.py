# Tic Tac Toe | Dec 2018 | Python


def display_instructions():
    print("Welcome to Tic-Tac-Toe!")
    print("""-------------------Instructions-------------------
Tic-Tac-Toe is played on a 9 square board, with the
objective of getting three of your marks in a row,
diagonal or straight. Marks are either an X or an O
-------------------Instructions-------------------""")
    print("""The board will be laid out as follows: 

                0 | 1 | 2
               -----------
                3 | 4 | 5
               -----------
                6 | 7 | 8
                    
You will make you move by entering a corresponding value.""")


def yes_no(question):
    answer = ""
    while answer.lower() != "y" or answer.lower() != "yes" or answer.lower() != "n" or answer.lower() != "no":
        print(question)
        answer = input("Enter Yes or No: ")
        if answer.lower() == "yes" or answer.lower() == "y":
            return "Yes"
        elif answer.lower() == "no" or answer.lower() == "n":
            return "No"
        else:
            continue


def ask_num(low, high, question):
    while True:
        answer = input(question)
        if answer.isdigit():
            if int(answer) in range(low, high+1):
                return int(answer)
            else:
                continue
        else:
            print("You must enter a digit: ")


display_instructions()
response = yes_no("Would you like to play? ")
ask_num(0, 8, "Enter a number, from 0 through 8: ")