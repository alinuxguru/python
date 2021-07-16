#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for z in range(0,4):
#   letters_password = letters.random
concatenate_letters = ''
#print(type(concatenate_letters))
for z in range(nr_letters):
  #print(random.choice(letters))
  concatenate_letters += random.choice(letters)
#print(concatenate_letters)  
  
concatenate_symbols = ''
for y in range(nr_symbols):
  concatenate_symbols += random.choice(symbols)
#print(concatenate_symbols)  

concatenate_numbers = ''
for y in range(nr_numbers):
  concatenate_numbers += random.choice(numbers)
#print(concatenate_numbers)

print(f"Sequential order Password: {concatenate_letters + concatenate_symbols + concatenate_numbers} ")

concat_list = [concatenate_letters, concatenate_symbols, concatenate_numbers]
#print(concat_list)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#random_list = ''
#for z in range(0, len(concat_list)):
concat_list2 = ''
random.shuffle(concat_list)
#print(concat_list)
#print(len(concat_list))
for z in range(0,len(concat_list)):
  concat_list2 += concat_list[z]

print(f"Randomized Password: {concat_list2}")
