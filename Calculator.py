                                    #CREATING CALCULATOR USING PYTHON

# Get input for 'a' while ensuring it's a valid float
while True:
    try:
        a = float(input("Type the value of 'a': "))
        break
    except ValueError:
        print("Please type an integer or a valid float.")

# Get input for 'b' while ensuring it's a valid float
while True:
    try:
        b = float(input("Type the value of 'b': "))
        break
    except ValueError:
        print("Please type an integer or a valid float.")

# Display a centered message
message = "We are going to create a calculator."
message = message.center(100)
print(message.upper())

# Display menu options
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Exponentiation")
print("5. Division\n6. Floor Division\n7. Modulus or Remainder")

# Get user's choice
while True:
    try:
        c = int(input("Type the chosen option (1-7): "))
        if 1 <= c <= 7:
            break
        else:
            print("Please type a number between 1 and 7.")
    except ValueError:
        print("Please type an integer.")

# Perform the selected operation
if c == 1:
    print(f"The addition of {a} and {b} is {round(a + b, 2)}")
elif c == 2:
    print(f"The subtraction of {a} and {b} is {round(a - b, 2)}")
elif c == 3:
    print(f"The multiplication of {a} and {b} is {round(a * b, 2)}")
elif c == 4:
    if b == 0:
        print(f"The exponentiation of {a} and {b} is 1")
    else:
        print(f"The exponentiation of {a} and {b} is {a ** b}")
elif c == 5:
    if b == 0:
        print(f"The division of {a} by {b} is undefined.")
    else:
        print(f"The division of {a} by {b} is {round(a / b, 2)}")
elif c == 6:
    if b == 0:
        print(f"The floor division of {a} by {b} is undefined.")
    else:
        print(f"The floor division of {a} by {b} is {a // b}")
else:
    print(f"The modulus or remainder of {a} and {b} is {round(a % b, 2)}")

# Add the standard if __name__ == "__main__": block
if __name__ == "__main__":
    print("This code is executed directly.")
