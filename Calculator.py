                                    #CREATING CALCULATOR USING PYTHON

def calculator():
    # Function to get a float input with validation
    def get_float(prompt):
        while True:
            try:
                value = input(prompt)
                return float(value)
            except:
                print("Invalid input type, enter a number.")

    # Map of operation symbols and numbers to operation codes
    operations_map = {
        '1': 'sum', '+': 'sum',
        '2': 'subtraction', '-': 'subtraction',
        '3': 'multiplication', '*': 'multiplication',
        '4': 'division', '/': 'division',
        '5': 'remainder', '%': 'remainder',
        '6': 'exponentiation', '**': 'exponentiation',
        '7': 'floor_division', '//': 'floor_division'
    }
    message = "We are going to create a calculator."
    print(message.center(100).upper())
    while True:
        a = get_float("Type the value of 'a': ")
        b = get_float("Type the value of 'b': ")

        print(
            "What do you want to perform? You can type the number or symbol:\n"
            "1 or + : Sum\n"
            "2 or - : Subtraction\n"
            "3 or * : Multiplication\n"
            "4 or / : Division\n"
            "5 or % : Remainder\n"
            "6 or **: Exponentiation\n"
            "7 or //: Floor Division"
        )

        while True:
            op_input = input("Type chosen option or symbol: ").strip()
            if op_input in operations_map:
                operation = operations_map[op_input]
                break
            else:
                print("Invalid choice. Enter 1-7 or a valid symbol (+, -, *, /, %, **, //).")

        if operation == 'sum':
            print(f"The sum of {a} and {b} is {a + b}.")
        elif operation == 'subtraction':
            print(f"The subtraction from {a} to {b} is {a - b}.")
        elif operation == 'multiplication':
            print(f"The multiplication of {a} with {b} is {a * b}.")
        elif operation == 'division':
            if b == 0:
                print(f"The division of {a} by {b} is undefined.")
            else:
                print(f"The division of {a} by {b} is {round(a / b, 2)}.")
        elif operation == 'remainder':
            print(f"The remainder when we divide {a} by {b} is {a % b}.")
        elif operation == 'exponentiation':
            print(f"The exponentiation of {a} and {b} is {a ** b}.")
        elif operation == 'floor_division':
            if b == 0:
                print(f"The floor division of {a} by {b} is undefined.")
            else:
                print(f"The floor division of {a} by {b} is {a // b}.")

        while True:
            try:
                cont = int(input("Type 1 to continue or 0 to stop: "))
                if cont in (0, 1):
                    break
                else:
                    print("Type 1 or 0 only.")
            except:
                print("Invalid input. Type integer 1 or 0 only.")

        if cont == 0:
            print("Ok, Thanks for using.")
            break


if __name__ == "__main__":
    calculator()