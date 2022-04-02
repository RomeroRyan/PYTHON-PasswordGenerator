# PYTHON Password Generator
- Ryan Romero         r.romero.softwaredev@gmail.com

# Project Description
A python password generator applciation with GUI. Upon running, users are able to click buttons that randomly generate a password (of either 12 or 16 char long). The passwords displayed will always have at least 1 captial letter, 1 lowercase letter, 1 symbol, and 1 number; these characteristics of strong passwords will always be met when a new password is generated. This was my final project in my Python Programming class, displaying what I learn in that class.

# Youtube Example Video
[![Watch the video](https://img.youtube.com/vi/6uKrE175ETg/maxresdefault.jpg)](https://youtu.be/6uKrE175ETg)

# How it Works (Summary)
User has a choice of 2 buttons upon running the application; both buttons generate a password, the only difference is the password length (12 and 16 characters). Clicking one of the 2 buttons triggers a function to generate a password. A random number will first choose if the current character being generated will be a number, symbol, captial, or lowercase. Each of the 4 categories has a list of all possible accepted characters saved in a dictionary data type. Once a category is choosen, a second random number is used to choose the corresponding character from the respective dictionary. The current character has now been choosen and appended to a string. This process loops until the full length of the password is generated

Once we generated the password, we must check that the password has atleast of of each of the 4 categories before displaying it to the user. The string will go through 4 different checks which make sures that the password includes atleast 1 number, 1 symbol, 1 captial and 1 lowercase. If all 4 check are successful, it displays the generated password on the GUI. If any of the 4 check failed, it cycles back to the top of the function and generates a new password untill the string passes all 4 checks.

# How to Run
Download the code from the repository
- Run ```PasswordGen.py```

# Ways to Improve
1. The code heavily relies on python's "**random**" libary to generate characters; Im aware that "**random**" libraries aren't truely random when it comes to computers and could affect the security of the passwords generated. A better random system can be implemented
2. While extremely unlikely, it is possible that code can gets stuck generating passwords that continue to fail the password strength checks. This could lead to a endless loop if the current user is extremely unlucky. To prevent this endless loop, we can implement code that will stop generating new passwords after multiple fail attempts.
3. When testing this code on different systems, it seems some systems allowed the user to copy/paste the generated password (as expected) however other systems did not. In order to prevent this situation, having a dedicated GUI button that copy the currently displayed password to the computer's clipboard would be very convenient. 
