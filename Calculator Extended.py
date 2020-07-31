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

def calculator():
    print ("Please choose from one of the following characters and enter it below: + , * , / , -")
    uInput = input("Here:")

    if uInput == ("+"):
        try:
            uInput1 = input("Enter a number here:")
            userNum1 = float(uInput1)

            uInput2 = input("Enter another number here:")
            userNum2 = float(uInput2)
        except:
            print("Please enter a valid number!")
            calculator()
        else:
            Result1 = userNum1 + userNum2
            Calculating(Result1)
    elif uInput == ("*"):
        try:
            uInput1 = input("Enter a number here:")
            userNum1 = float(uInput1)

            uInput2 = input("Enter another number here:")
            userNum2 = float(uInput2)
        except:
            print("Please enter a valid number!")
            calculator()
        else:
            Result2 = userNum1 * userNum2
            Calculating(Result2)
    elif uInput == ("/"):

        uInput1 = input("Enter a number here:")
        userNum1 = float(uInput1)

        uInput2 = input("Enter another number here:")
        userNum2 = float(uInput2)
        if userNum2 == 0:
            Calculating()
            print("\n",userNum1,"/0 is undefined, please try something else.")
            calculator()
        else:
            Result3 = userNum1 / userNum2
            Calculating(Result3)
    elif uInput == ("-"):
        try:
            uInput1 = input("Enter a number here:")
            userNum1 = float(uInput1)

            uInput2 = input("Enter another number here:")
            userNum2 = float(uInput2)
        except:
            print("Please enter a valid number!")
            calculator()
        else:
            Result4 = userNum1 - userNum2
            Calculating(Result4)
    else:
       print("Please enter a character from the list.")
       calculator()

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