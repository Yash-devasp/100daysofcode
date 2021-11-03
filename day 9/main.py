from logo import logo
from os import system

bid_dtl = {}
next_bid = True

print(logo)
while next_bid:
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))
    should_continue = input("Are there any others bidders? Type 'yes' or 'no'.\n")
    bid_dtl[name] = bid_amount
    if should_continue == 'no':
        next_bid = False
    else:
        system('clear')

winner = max(bid_dtl,key=bid_dtl.get)
print(f"The winner is {winner} with a bid of ${bid_dtl[winner]}")