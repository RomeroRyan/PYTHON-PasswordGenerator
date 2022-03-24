# PYTHON Password Generator
- Ryan Romero         r.romero.softwaredev@gmail.com

# Project Description
A simple password generator applciation with GUI. Upon running, users are able to click buttons that will randomly generate a password. The passwords displayed will always have at least 1 captial letter, 1 lowercase letter, 1 symbol, and 1 number; these characteristics of strong passwords will always be met when a new password is generated.

# Youtube Example Video
[![Watch the video](https://img.youtube.com/vi/6uKrE175ETg/maxresdefault.jpg)](https://youtu.be/6uKrE175ETg)

# How it Works (Summary)
User has a choice of 2 buttons upon running the application; both buttons generate a password, the only difference is the password length. Clicking one of the 2 buttons triggers a function to generate a password. It enters a loop where a random number will first choose if the character generating in current loop iteration will be a number, symbol, captial, or lowercase. Each of the 4 categories has a list of all possible generated characters saved in a dictionary data type. A second random number is used to choose the corresponding character from the respective dictionary and saved it onto a string. Once it exit the loop, the string is holding the randomly generated password which goes through 4 different checks which make sures that the password includes atleast 1 number, symbol, captial and lowercase. If all 4 check are successful, it displays the generated password on the GUI. If any of the 4 check failed, it cycles back to the top of the function and generates a new password untill the string passes all 4 checks.

# How to Run
1. Download the code from the repository
2. run ```PasswordGen.py```

# Ways to Improve
1. The code heavily relies on python's "**random**" libary to generate characters; Im aware that random libraries arent truely random when it comes to computer and could affect the security of the passwords generated
2. While extremely unlikely, it is possible that code continues to generate passwords that fail the password strength checks. This could lead to a endless loop if the current user is extremely unlucky and continues to generate passwords that are too weak. To prevent this endless loop, we can implement code that will stop generating new passwords after multiple fail attempts.
