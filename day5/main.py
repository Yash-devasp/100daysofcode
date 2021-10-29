import string
import random

letters = list(string.ascii_letters)
digits = list(string.digits)
symbol = list(string.punctuation)

print("Welcome to the PyPassword Generator!")

letter_count = int(input("How many letters would you like in your password?\n"))

symbol_count = int(input("How many symbols would you like?\n"))

number_count = int(input("How many numbers would you like?\n"))

rand_letters = random.choices(letters,k=letter_count)
rand_symbols = random.choices(symbol,k=symbol_count)
rand_numbers = random.choices(digits,k=number_count)

res = rand_letters + rand_numbers + rand_symbols
random.shuffle(res)
res_str = "".join(res)
print(res_str)