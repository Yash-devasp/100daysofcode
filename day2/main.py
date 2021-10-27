print("Welcome to the tip calculator.")

amount = float(input("What was the total bill? $"))

num_of_people = int(input("How many people to split the bill? "))

percent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

per_person = (amount + ((percent / 100) * amount)) / num_of_people

print(f"Each person should pay: ${round(per_person,1)}")