                                    #CREATING CALCULATOR USING PYTHONy

def calculator():
    # Loop to get the first number from the use
    while True:
        try:
            a = input("Type the value of 'a': ") # Prompt user for input
            a = float(a)  # Convert input to float
            break  # Exit loop on successful conversion
        except:
            print("Invalid input type only integer.")

    # Loop to get the second number from the user
    while True:
        try:
            b = input("Type the value of 'b': ") # Prompt user for input
            b = float(b) # Convert input to float
            break # Exit loop on successful conversion
        except:
            print("Invalid input type only integer.")
    
    # Display a welcome message
    message = "We are going to create a calculator."
    message = message.center(100) # Center the message
    print(message.upper()) # Print message in uppercase

    # Display operation options to the user
    print("What you want to perform.\n1.Sum\n2.Substration\n3.Multiplicaltion\n4.Divide\n5.Remender\n6.Exponentiation\n7.Floor Division")

    # Loop to get the operation choice from the user
    while True:
       try:
            Operation = input("Type chosen option: ")  # Prompt user for operation choice
            Operation = int(Operation)  # Convert input to integer
            if Operation<=7 and Operation>0:  # Check if the choice is valid
               break  # Exit loop on valid input
            else:
                print("Type integer between 1 to 7 only.")
       except:
           print("Type integer only.")
    
    # Perform the chosen operation and display the result
    if Operation == 1:
        # Calculate the sum of a and b
        print(f"The sum of {a} and {b} is {a+b}.")
    elif Operation==2:
        # Calculate the subtraction of a and b
        print(f"The subtraction from {a} to {b} is {a-b}.")
    elif Operation==3:
        # Calculate the multiplication of a and b
        print(f"The multiplication of {a} with {b} is {a*b}.")
    elif Operation==4:
        if b == 0:
            # Handle division by zero
            print(f"The division of {a} by {b} is undefined.")
        else:
            # Calculate the division of a and b
            print(f"The division of {a} by {b} is {round(a / b, 2)}")
    elif Operation==5:
        # Calculate the remainder of a and b
        print(f"The remender when we divide {a} by {b} is {a%b}.")
    elif Operation==6:
        if b == 0:
            # Handle exponentiation with zero
            print(f"The exponentiation of {a} and {b} is 1")
        else:
            # Calculate the exponentiation of a and b
            print(f"The exponentiation of {a} and {b} is {a ** b}")
    elif Operation == 7:
        # Calculate the floor division of a and b
        if b == 0:
            # Handle floor division with zero
            print(f"The floor division of {a} by {b} is undefined.")
        else:
            print(f"The floor division of {a} by {b} is {a // b}")


    # Loop to ask the user if they want to continue
    while True:
        try:
            s = input("type 1 for continue/0 for stop: ") # Prompt user to continue or stop
            s = int(s) # Convert input to integer
            if s == 1 or s == 0: # Check if input is valid
                if  s == 0:
                    print("Ok, Thanks for using.")
                    break # Exit the loop if the user chooses to stop
                else:
                    # Get new values for a and b with input checks
                    while True:
                            try:
                                a = input("Type the value of 'a': ") # Get new value for a
                                a = float(a)  # Convert input to float
                                break  # Exit loop on successful conversion
                            except:
                                print("Invalid input type onlinteger.")
                    while True:
                            try:
                                b = input("Type the value of 'b': ")  # Get new value for b
                                b = float(b)  # Convert input to float
                                break # Exit loop on  successful conversion
                            except:
                                print("Invalid input type only integer.")
                
                # Display operation options again
                print("What you want to perform.\n1.Sum\n2.Substration\n3.Multiplicaltion\n4.Divide\n5.Remender\n6.Exponentiation\n7.Floor Division")
                while True:
                    try:
                        Operation = input("Type chosen option: ") # Get new operation choice
                        Operation = int(Operation)  # Convert input to integer
                        if Operation<=7 and Operation>0:  # Check if the choice is valid
                            break  # Exit loop on valid input
                        else:
                            print("Type integer between 1 to 7 only.")
                    except:
                        print("Type integer only.")
                
                # Perform the operation and display the result
                if Operation == 1:
                    # Calculate the sum of a and b
                    print(f"The sum of {a} and {b} is {a+b}.")
                elif Operation==2:
                    # Calculate the subtraction of a and b
                    print(f"The subtraction from {a} to {b} is {a-b}.")
                elif Operation==3:
                    # Calculate the nultiplication of a and b
                    print(f"The multiplication of {a} with {b} is {a*b}.")
                elif Operation==4:
                    if b == 0:
                        # Handle division by zero
                        print(f"The division of {a} by {b} is undefined.")
                    else:
                        # Calculate the division of a and b
                        print(f"The division of {a} by {b} is {round(a / b, 2)}")
                elif Operation==5:
                    # Calculate the remainder of a and b
                    print(f"The remender when we divide {a} by {b} is {a%b}.")
                elif Operation==6:
                    if b == 0:
                        # Handle exponentiation with zero
                        print(f"The exponentiation of {a} and {b} is 1")
                    else:
                        # Calculate the exponentiation of a and b
                        print(f"The exponentiation of {a} and {b} is {a ** b}") 
                elif Operation == 7:
                    # Calculate the floor division of a and b
                    if b == 0:
                        # Handle floor division with zero
                        print(f"The floor division of {a} by {b} is undefined.")
                    else:
                        print(f"The floor division of {a} by {b} is {a // b}")
            else:
                print("Type 1 or 0 only.")      
        except:
            print("Type integer only.")

# Add the standard if __name__ == "__main__": block
if __name__ == "__main__":
    # Call the calculator function          
    calculator()