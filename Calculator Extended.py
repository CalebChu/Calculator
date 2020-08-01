import time
import sys
timeout = time.time() + 2
def Calculating (Results):
    print('\rCalculating', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    ...
    print('\rCalculating.', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    ...
    print('\rCalculating..', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)
    ...
    print('\rCalculating...', end=" ")
    sys.stdout.flush()
    time.sleep(0.5)

    print('\r', Results, end=" ")


def getNumber(message):
    validInput = False
    while validInput == False:
        userChoice = input(message)
        if userChoice.isnumeric():
            validInput = True
        else:
            print("Please enter a valid number.")
    return float(userChoice)

def getOperation(message):
    validInput = False
    operatorList = ["+","-","*","/"]
    while validInput == False:
        userChoice = input(message)
        if userChoice in operatorList:
            validInput = True
        else:
            print("Please enter a valid operation.")
    return userChoice



def calculator():
    operationInput = getOperation("Please choose from one of the following characters and enter it below: + , * , / , -\n")
    userNum1 = getNumber("Enter a number here:")
    userNum2 = getNumber("Enter another number here:")

    if operationInput == ("+"):
        Result = userNum1 + userNum2
    elif operationInput == ("*"):
        Result = userNum1 * userNum2
    elif operationInput == ("-"):
        Result = userNum1 - userNum2
    elif operationInput == ("/"):
        if userNum2 != 0:
            Result = userNum1 / userNum2
        else:
            print(userNum1, "/0 is undefined, please try something else.")
    else:
       print("Please enter a character from the list.")
    Calculating(Result)


def yesNoQuestion(question):

    validAnswer = False
    while validAnswer == False:
        time.sleep(0.5)
        yesno = input("\nWould you like to continue?\n")
        if yesno.lower() == "yes" or yesno.lower() == "y":
            print("Let's continue")
            validAnswer = True
        elif yesno.lower() == "no" or yesno.lower() == "n":
            print("Goodbye!")
            validAnswer = True
        else:
            print("Please answer with 'yes' or 'no'")
    return yesno


def mainLoop():
    yesno = "yes" or "y"
    while yesno.lower() == "yes" or yesno.lower() == "y":
        calculator()
        yesno = yesNoQuestion("Would you like to continue?")



mainLoop()