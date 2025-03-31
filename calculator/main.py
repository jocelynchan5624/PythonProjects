from art import logo

def calculator(operator, first_number, next_number):
    result = 0
    if operator == '+':
        result = first_number + next_number
    elif operator == '-':
        result = first_number - next_number
    elif operator == '*':
        result = first_number * next_number
    elif operator == '/':
        result = first_number / next_number
    else:
        result = 'Invalid Operator'
    return result

def calculator_software():
    accumulate_calculation = True
    first_number = int(input("What's the first number? "))

    while accumulate_calculation:
        print("+\n-\n*\n/")
        operator = input("Pick an operator: ")
        next_number = int(input("What's the next number? "))
        calculator(operator, first_number, next_number)
        answer = f"{first_number} {operator} {next_number} = {calculator(operator, first_number, next_number)}"
        print(answer)
        ask_to_continue = ''
        while ask_to_continue == '':
            ask_to_continue = input(f"Type 'y' to continue the calculation with {calculator(operator, first_number, next_number)} "
                                    f"or 'n' to start a new calculation or 'exit' to end: ")
            if ask_to_continue == 'n':
                accumulate_calculation = False
                calculator_software()
            elif ask_to_continue == 'y':
                if calculator(operator, first_number, next_number) != "Invalid Input":
                    first_number = calculator(operator, first_number, next_number)
            elif ask_to_continue == 'exit':
                return
            else:
                print("Invalid response. Try again!")
                ask_to_continue = ''

print(logo)
calculator_software()