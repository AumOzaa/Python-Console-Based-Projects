# Number guessing game :
from random import randint
from winreg import error


toContinue = True

def toInt(num):
    try:
        int(num)
        return True
    except ValueError:
        print("Enter a number!")
        return False

while(toContinue):
    random_number = randint()
    user_input = input("Enter number to guess: ")
    if(toInt(user_input)):
        if(int(user_input) == random_number):
            print("You have won!")
            print("Do you wish to continue?")
            print("Press 1: To continue")
            user_input_2 = input("Press 2: To exit\n")

            if(user_input_2 == 2) :
                toContinue = False
        else:
            print("OOps! You guessed the wrong number!")
            print("Better luck next time!")
            print("Do you wish to continue?")
            print("Press 1: To continue")
            user_input_2 = input("Press 2: To exit\n")
            if (user_input_2 == 2):
                toContinue = False
    else:
        print("Do not enter anything else than number!")
        print("Do you wish to continue?")
        print("Press 1: To continue")
        user_input_2 = input("Press 2: To exit\n")
        if (user_input_2 == 2):
            toContinue = False