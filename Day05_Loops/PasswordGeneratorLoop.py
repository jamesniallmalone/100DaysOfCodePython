#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n")) 
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
#Chose characters for the password, order doesn't matter here, so we can add chars in one go, symbols in one go, numbers in one go
for char in range(1, number_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, number_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, number_numbers + 1):
  password_list += random.choice(numbers)

#Shuffle the order of the letters
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")