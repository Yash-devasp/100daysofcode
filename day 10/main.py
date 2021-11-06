from logo import logo
from os import system

def add(first_number,second_number):
    return first_number + second_number

def subtract(first_number,second_number):
    return first_number - second_number

def multiply(first_number,second_number):
    return first_number * second_number

def divide(first_number,second_number):
    return first_number / second_number

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    first_number = float(input("What's the first number? "))
    for op in operators:
        print(op)
    should_continue = True
    while should_continue:
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number? "))
        calc = operators[operator]
        res = calc(first_number,second_number)
        print(f"{first_number} {operator} {second_number} = {res}")
        yes_or_no = input(f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ").lower()
        if yes_or_no == "y":
            first_number = res
        else:
            should_continue = False
            system("clear")
            calculator()

calculator()