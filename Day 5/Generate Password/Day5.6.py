#Easy Level in Generate the password with out the order

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level in Generate the password with  the order
genr_letters = random.choices(letters , k = nr_letters)
genr_symbols = random.choices(numbers,k= nr_symbols)
genr_numbers = random.choices(symbols,k=nr_numbers)
password = genr_letters + genr_symbols + genr_numbers
letters = ""
for letter in password:
    letters += letter     
    
print(f"Your Generated password is : {letters}")

#The Hard level is to change the order of the letters

print("---------------------------------------------------")
random.shuffle(password)
FinalPassword = ""
for letter in password :
    FinalPassword += letter 
print(f"The Password after reorder the letters is : {FinalPassword}")
print("------------------------------------------------------------")

