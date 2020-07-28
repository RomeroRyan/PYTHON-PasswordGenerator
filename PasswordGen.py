# Project Began July 20 2020 by Ryan Romero
from tkinter import *
import random

# ----- DICTIONARIES -----
SymbolDict = {
    1: "!",
    2: "#",
    3: "$",
    4: "%",
    5: "&",
    6: "(",
    7: ")",
    8: "*",
    9: "+",
    10: "-",
    11: "/",
    12: "?",
    13: ":",
    14: ";",
    15: "<",
    16: ">",
    17: "=",
    18: "@",
    19: "[",
    20: "]",
    21: "^",
    22: "{",
    23: "}",
}

UpperDict = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
    5: "E",
    6: "F",
    7: "G",
    8: "H",
    9: "I",
    10: "J",
    11: "K",
    12: "L",
    13: "M",
    14: "N",
    15: "O",
    16: "P",
    17: "Q",
    18: "R",
    19: "S",
    20: "T",
    21: "U",
    22: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z",
}

LowerDict = {
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
}


# ----- HELPER FUNCTIONS ------
# return random number
def RandomNum():
    num = random.randint(0,9)
    return str(num)

# return random symbol from dictionary
def RandomSymbol():
    randomInt1 = random.randint(1, 23)
    return SymbolDict[randomInt1]

# returns random capital letter from dictionary
def RandomLetterUpper():
    randomInt2 = random.randint(1,26)
    return UpperDict[randomInt2]

# return random lowercase letter from dictionary
def RandomLetterLower():
    randomInt3 = random.randint(1, 26)
    return LowerDict[randomInt3]

# checks if string has atleast 1 number
def HasNumber(password):
    if( any(char.isdigit() for char in password) ):
        return True
    else:
        print("failed Number Test")
        return False

# checks if string has atleast 1 symbol   
def HasSymbol(password):
    if( any(not char.isalnum() for char in password) ):
        return True
    else:
        print("failed Symbol Test")
        return False

# checks if string has atleast 1 capital letter      
def HasUpper(password):
    if( any(char.isupper() for char in password) ):
        return True
    else:
        print("failed Upper Test")
        return False

# check if string has atleast 1 lowercase letter    
def HasLower(password):
    if (any(char.islower() for char in password)):
        return True
    else:
        print("failed Lower Test")
        return False


# ----- MAIN FUNCTIONS -----
# this function generates the password
def GeneratePassword(size):
    
    # flag used to exit function loop. if password has atleast 1 num/symbol/upper/lower, flag is set off and exits loop
    # otherwise starts over and generates a new password
    flag = 0
    while(flag == 0):

        # clear passwordHolder and charHolder
        passwordHolder = ""
        charHolder = ""

        # main loop. Generates random char every iteration
        count = 0
        while(count < size):
            # this random num used to determine if char generated is a num, symbol, upper, or lowercase
            randomVal = random.randint(1, 4)
            
            if(randomVal == 1):
                charHolder = RandomNum()
            elif(randomVal == 2):
                charHolder = RandomSymbol()
            elif(randomVal == 3):
                charHolder = RandomLetterUpper()
            elif(randomVal == 4):
                charHolder = RandomLetterLower()
            else:
                charHolder = "  "
    
            # add the generated char to the string holding full password
            passwordHolder = passwordHolder + str(charHolder)
            count = count + 1

        #check password has 1 of each, if so, change flag to true and exit function loop
        if(HasNumber(passwordHolder)):
            if(HasSymbol(passwordHolder)):
                if(HasUpper(passwordHolder)):
                    if(HasLower(passwordHolder)):
                        flag = 1

    # print out generated password onto window
    thePassword.config(text=passwordHolder)


# ----- GUI CODE -----
# create the GUI window
MainWindow = Tk()
MainWindow.title("Generator App")
MainWindow.geometry("300x100")

# frames
topFrame = Frame(MainWindow)
topFrame.pack(side=TOP)
botFrame = Frame(MainWindow)
botFrame.pack(side=BOTTOM)

# Label
titleLabel = Label(topFrame, text="Password Generator", font= "bold")
thePassword = Label(topFrame, text="-sample-")
emptyLabel = Label(topFrame, text = " ")

# button
generateButton = Button(botFrame, text="Generate!", command= lambda: GeneratePassword(12))                # note to self: Lamda allows method to be called with an argument
generateButton2 = Button(botFrame, text= "Generate Long!", command= lambda: GeneratePassword(16))

# organize GUI
titleLabel.pack()
emptyLabel.pack()
thePassword.pack()
generateButton.grid(row=0, column=0)
generateButton2.grid(row=0, column=1)

# Ending of GUI Window
MainWindow.mainloop()
