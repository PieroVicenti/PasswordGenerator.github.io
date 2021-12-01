# PasswordGenerator.github.io

Project with the aim of generating a random password based on the user input and necessity. 


**LOGIC OF THE APP**
User has to input the number of letters he desires in his password, the number of  numbers and the number of symbols (For example, I can ask the system to generate a password with 10 letters, 5 numbers, and 6 symbols).

**LISTS**
LIST OF LETTERS, NUMBERS, AND SYMBOLS TO GENERATE PASSWORDS:

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
           
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

**FINAL STEPS**
There is no range, the password can be as long as required.
As soon as the three values have been specified, a random password will be generated, shuffling numbers, symbols, and letters.
The random.shuffle method makes the password a strong password.
