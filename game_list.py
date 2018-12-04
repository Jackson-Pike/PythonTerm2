# Blah

game_list = []


def game_display():
    for i in range(len(game_list)):
        print(str(i+1) + ". " + game_list[i])


while True:
    print("""
    1 - Add to list
    2 - Remove from list
    3 - Insert
    4 - Display Current List
    5 - Quit
    """)
    init = input("")
    if init.isdigit():
        opt = int(init)
        if opt == 1:
            game_append = input("What game would you like to add to your list?: ")
            game_list.append(game_append)
            game_display()

        elif opt == 2:
            game_display()
            game_remove = input("What game would you like to remove from your list?: ")
            if game_remove in game_list:
                q = input("Are you sure you want to remove \"" + game_remove + "\" from your list?: ")
                if q.lower() == "yes" or q.lower() == "y":
                    game_list.remove(game_remove)
                    print("\"", game_remove, "\" was removed from your list. Your list is now as follows: ")
                    game_display()
                elif q.lower() == "no" or q.lower() == "n":
                    print("Your game was not removed.")
            elif game_remove.isdigit():
                del game_list[int(game_remove)-1]
            else:
                print("Error: \"" + game_remove + "\" was not found in your list")
        elif opt == 3:
            game_insert = input("What game would you like to insert into list?")
            position = int(input("At what position would you like to place \"" + game_insert + "\" in your list?"))
            position -= 1

            while True:
                if position < len(game_list):
                    game_list.insert(position, game_insert)
                    game_display()
                    break
                else:
                    print("Invalid Position!")
        elif opt == 4:
            if len(game_list) > 0:
                game_display()
            else:
                print("List is currently empty. ")
        elif opt == 5:
            quitq = input("Are you sure you want to quit? :")
            if quitq.lower() == "yes" or quitq.lower() == "y":
                print("Okay!")
                break
            else:
                continue

    elif init.lower() == "quit" or init.lower() == "q":
        print("Goodbye!")
        break
    else:
        print("Not a valid input!!")
        continue

