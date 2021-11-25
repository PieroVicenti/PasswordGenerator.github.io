import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

question_letters = int(input("How many letters do you want?"))
question_numbers = int(input("How many numbers do you want?"))
question_symbols = int(input("How many symbols do you want?"))

password_list = []
for char in range(1, question_letters + 1):
    random_char = random.choice(letters)
    password_list += random_char

for char in range(1, question_numbers + 1):
    random_char = random.choice(numbers)
    password_list += random_char

for char in range(1, question_symbols + 1):
    random_char = random.choice(symbols)
    password_list += random_char

password = " "
for char in password_list:
    password += char

print(password)