my_list = [" ", "O", " "]


def list_shuffle(my_list):
    from random import shuffle
    shuffle(my_list)
    return my_list


players_guess = None
while players_guess not in [0, 1, 2]:
    players_guess = int(input("guess the number 0,1 or 2 "))
    if players_guess > 2:
        print("input invalid")

shuf_list = list_shuffle(my_list)


def check_guess(guess, my_list):
    if my_list[guess] == "O":
        print("Correct ! ! !")
        print(my_list)
    else:
        print("Wrong ! ! ! !")
        print(my_list)


check_guess(players_guess, my_list)
