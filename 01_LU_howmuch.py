# Lucky Unicorn Decomposition Step 1
# Get intial amount and check that it's valid

# Number checking function goes here
def intcheck(question, low, high):
    valid = False
    error = "Whoops! Please enter an integer between {} and {}".fromat(low, high,)
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

# main routine goes here

keep_going = ""
while keep_going == "":
    how_much = intcheck("How much money do you want to play with? ", 1, 10)
    print("You have chosen to play with ${}".format(how_much))

    keep_going = input("Again?")
