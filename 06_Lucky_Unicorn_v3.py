# Lucky Unicorn Fully Working Program
# Program should work - needs to be tested for usability

import random


# Inter checking function below
def intcheck(question, low, high):
    valid = False
    error = "Whoops! Please enter an integer between {} and {}".format(low, high,)
    while not valid:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print(error)
                print()
        except ValueError:
            print(error)
# function to print out 'token statements'. Takes in message and then apllies 'decoration' to top
# and bottom of message based on a specified charater
def token_statement(statement, char):
print()
print(char * len(statement))
print(statement)
print(char * len(statement))
print()

# main routine
# Cost Payout Constants
COST = 1  # cost per round
UNICORN = 5  # unicorn wins $5
ZEBRA_HORSE = 0.5  # zebra / horse 'wins' 50c
DONKEY = 0  # donkey does not win anything

# Introduction / Instructions

print("**** Welcome to the Lucky Unicorn Game")
print()
print("To play, enter an amount of money between $1 and $10 (whole dollars only).")
print()
print("- IT costs $1/round")
print()
print("Payouts...")
print("- Unicorn: ${:.2f}".format(UNICORN))
print("- Horse / Zebra: {:.2f}".format(ZEBRA_HORSE))
print("- Donkey: {:.2f}".format(DONKEY))
print()

# main routine goes here

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How mcuh money would you like to play with? ", 1, 10)
round_count = 0

keep_going = ""
while keep_going == "":

    # tokens list includes 10 times to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse"
              "zebra", "zebra", "zebra"
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()
    print("You got a {}".format(token))

    # Adjust total correctly for a given token
    if token == "unicorn":
        token_statement("***** Congratulations! it's a ${:.2f} {} *****".format(UNICORN, token), "*")
        balance += UNICORN

    elif token == "donkey":
        token_statement("-- Sorry. it's a {}. you did not win anything this round --".format(token),"-")
        balance -= COST

    else:
        token_statement("^^ Good try . it's a {}.")


    print()

    print(feedback)
    print("You have {} to play with".format(balance))
    print()

    if balance < 1:
        print("Sorry you don't have enough money to continue. Gmae over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit") \

# farewell user at the end of game
print("Thank you for playing.")


