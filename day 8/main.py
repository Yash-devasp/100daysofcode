import string
from logo import logo

go_again = True
letter = list(string.ascii_lowercase)

def encode(message,shift):
    res = ""
    for l in message:
        loc = letter.index(l)
        new_loc = (loc + shift) % 26
        res += letter[new_loc]

    return res

def decode(message,shift):
    res = ""
    for l in message:
        loc = letter.index(l)
        new_loc = (loc - shift)
        res += letter[new_loc]

    return res

print(logo)

while go_again:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if choice == "encode":
        print(f"Here's the encoded result: {encode(message,shift)}")
    else:
        print(f"Here's the decoded result: {decode(message,shift)}")

    next_step = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if next_step == "no":
        print("Goodbye")
        go_again = False