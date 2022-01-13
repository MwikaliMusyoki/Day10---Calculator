from art import logo


def add(n1, n2):
    '''Function recieves two numbers and returns their sum'''
    return n1 + n2


def subtract(n1, n2):
    '''Function recieves two numbers and returns their difference'''
    return n1 - n2


def multiply(n1, n2):
    '''Function recieves two numbers and returns the result after multiplying them'''
    return n1 * n2


def devide(n1, n2):
    '''Function recieves two numbers and returns the result of deviding them'''
    return n1 / n2


def calculator():
    print(logo)

    num1 = float(input("What's the first number? \n"))

    operators = {"+": add, "-": subtract, "*": multiply, "/": devide}

    for key in operators:
        print(key)

    exit_calc = False

    while exit_calc == False:
        operation = input("Pick an operator")
        num2 = float(input("What's the next number? \n"))
        calculation = operators[operation]
        answer = calculation(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        if input(f"To continue calculating with {answer} type 'y' . Type 'n' to start a fresh calculation ") == "y":
            num1 = answer
        else:
            exit_calc = True
            calculator()


calculator()
