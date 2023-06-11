import random

def heads_or_tails():

    # 1 = heads
    # 2 = tails

    #get user input
    user_input = input("Enter heads or tails: ")

    #get random number
    random_number = random.randint(1, 2)

    #check if user won
    if user_input == "heads" and random_number == 1:
        print("You won!")
    elif user_input == "tails" and random_number == 2:
        print("You won!")
    else:
        print("You lost!")
        
heads_or_tails()