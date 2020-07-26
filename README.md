# -Project-3-PYTHON-Password-Generator (Project 3)
A simple Python application with GUI. Upon running, users are able to click 2 buttons that will randomly generate a password. The passwords displayed will always have 1 atleast 1 captial letter, 1 lowercase letter, 1 symbol, and 1 number.

## -How-it-Works (summary):
Clicking one of the 2 buttons triggers a function to generate a password. It enters a loop where a random number will first choose if the character generating in current loop iteration will be a number, symbol, captial, or lowercase. Each of the 4 categories has a list of all possible generated characters saved in a dictionary data type. A second random number is used to choose the corresponding character from the respective dictionary and saved it onto a string. Once it exit the loop, the string is holding the randomly generated password which goes through 4 different checks which make sures that the password includes atleast 1 number, symbol, captial and lowercase. If all 4 check are successful, it displays the generated password on the GUI. If any of the 4 check failed, it cycles back to the top of the function and generates a new password untill the string passes all 4 checks.

### -CONTACTS:
    Ryan Romero     r.romero.softwaredev@gmail.com
    LinkedIn:       (TBA)

### -Notes:
1. The code heavily relies on python's **random** libary to generate characters; I am unaware how truely random the libary's logic is.
2.

### -Ways-to-Improve-Code:
1. While very unlikely, it is possible that code continues to generate passwords that fail the check everytime. Creating a failsafe to prevent code from being stuck in an endless loop (have it exit the loop after 3 or 4 fails and display an error message)
2. 
