import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

symbol = [rock,paper,scissor]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(symbol[choice])

print("Computer chose:")
computer = random.randint(0,2)

print(symbol[computer])

win_message = "You win!"
if choice == 0 and computer == 2:
    print(win_message)
elif choice == 1 and computer == 0:
    print(win_message)
elif choice == 2 and computer == 1:
    print(win_message)
elif choice == computer:
    print("It's a draw")
else:
    print("You lose")