# Guess number game | November 2018 | author @ Jackson Pike

import random


def menu() -> object:
    print("Hello! Welcome to Jackson Pike's Guess My Number Game\nEnter Option:\n1. Play Game")
    print("2. Custom Game\n3. Credits\n4. Exit")
    menu_choice = input()
    if menu_choice == "1" or menu_choice == "1.":
        get_number()


def get_number():
    number = random.randrange(1, 100)
    print(number)
    attempts = 5
    attempts_completed = 0
    guess_number(number, attempts, attempts_completed)


def guess_number(number, attempts, attempts_completed):
    while attempts > 0 and attempts_completed <= 5:
        usr_guess = input("Enter Guess: ")
        if usr_guess.isdigit() and usr_guess != number:
            usr_guess = int(usr_guess)
            attempts -= 1
            if usr_guess > number:
                print("Sorry! Your guess was too high, try a lower guess.")
                print("You have", attempts, "attempts left.")
                guess_number(number, attempts, attempts_completed)
            elif usr_guess < number:
                print("Sorry! Your guess was too low, try a higher guess.")
                print("You have", attempts, "attempts left.")

            elif usr_guess == number:
                guess_number_win()
                break
        else:
            print("Invalid input! Please enter a whole number.")
            guess_number(number, attempts, attempts_completed)
    guess_number_loose()

def guess_number_loose():
    print("Sorry! You took too many attempts. ")



def guess_number_win():
    print("Nice! You won!")


menu()
