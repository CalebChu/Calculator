import time
import sys
import tkinter as tk


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


# GUI code --------------------------------------------------------------------------------------------------------------

class GUI:

    def renderInstructions(self, parent, background):
        label = tk.Label(master=parent, text="Instructions:", bg=background)
        label.grid(row=0, column=0)
    
    def renderCalculations(self, parent, background):
        label = tk.Label(master=parent, text="Calculations:", bg=background)
        label.grid(row=0, column=0)
    
        entry = tk.Entry(master=parent, width=50, fg="black", bg="white")
        entry.grid(row=1, column=0)
    
    def addButton(self, window, r, c, message ):
        button = tk.Button(master=window, text=message)
        button.grid(row=r, column=c, sticky="nsew")

        def handleClick(event):
            print("The button was clicked: " + message)

        button.bind("<Button-1>", handleClick)
    
    
    def renderButtons(self, parent):
        TOTAL_ROWS=4
        TOTAL_COLUMNS=4
        
        for row in range(TOTAL_ROWS):
            parent.rowconfigure(row, weight=1, minsize=50)
    
        for column in range(TOTAL_COLUMNS):
            parent.columnconfigure(column, weight=1, minsize=75)
    
        FIRST_ROW=0
        self.addButton(parent, FIRST_ROW, 0, "1")
        self.addButton(parent, FIRST_ROW, 1, "2")
        self.addButton(parent, FIRST_ROW, 2, "3")
    
        SECOND_ROW=1
        self.addButton(parent, SECOND_ROW, 0, "4")
        self.addButton(parent, SECOND_ROW, 1, "5")
        self.addButton(parent, SECOND_ROW, 2, "6")
    
        THIRD_ROW=2
        self.addButton(parent, THIRD_ROW, 0, "7")
        self.addButton(parent, THIRD_ROW, 1, "8")
        self.addButton(parent, THIRD_ROW, 2, "9")
    
        FOURTH_ROW=3
        self.addButton(parent, FOURTH_ROW, 0, "ENTER")
        self.addButton(parent, FOURTH_ROW, 1, "0")
    
        OPERATOR_COLUMN = 3 
        self.addButton(parent, 0, OPERATOR_COLUMN, "+")
        self.addButton(parent, 1, OPERATOR_COLUMN, "-")
        self.addButton(parent, 2, OPERATOR_COLUMN, "*")
        self.addButton(parent, 3, OPERATOR_COLUMN, "/")
    
        return parent
    
    
    def handle_keypress(self,event):
        print("Key pressed: " + event.char)
    
    def handle_click(self,event):
        print("The button was clicked!" )
    
    def attachEventHandlers(self,window):
        window.bind("<Key>", self.handle_keypress)
    
    def drawWindow(self):
        WIDTH = 220
        HEIGHT = 100
    
        window = tk.Tk()
        
        FRAME1_BACKGROUND="black"
        frame1 = tk.Frame(master=window, width=WIDTH, height=HEIGHT, bg=FRAME1_BACKGROUND)
        self.renderInstructions(frame1, FRAME1_BACKGROUND)
        frame1.pack(fill=tk.Y, side=tk.LEFT)
    
        FRAME2_BACKGROUND="gray"
        frame2 = tk.Frame(master=window, width=WIDTH, height=HEIGHT, bg=FRAME2_BACKGROUND)
        self.renderCalculations(frame2, FRAME2_BACKGROUND)
        frame2.pack(fill=tk.Y, side=tk.LEFT)
    
        frame3 = tk.Frame(master=window, width=WIDTH, height=HEIGHT)
        self.renderButtons(frame3)
        frame3.pack(fill=tk.Y, side=tk.LEFT)
    
        self.attachEventHandlers(window)

        return window
    

gui = GUI()

window = gui.drawWindow()

window.mainloop()

#mainLoop()
