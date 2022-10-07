import random

def RollDice():
    random_number = random.randrange(1,7)
    return random_number

print("Dice Rolling Simulator")
while True:
    option = input("Do you want to roll the dice? YES or NO?\n").upper()

    if option == "YES":
        random_number = RollDice()
        print("Number: " + str(random_number))
    elif option == "NO":
        print("See you later!")
        exit()
    else:
        print("Type YES or NO to continue with the program!")