# Simple-Calculator
 This Python script is a simple calculator capable of performing a number of arithmetics depending on a user's input choice. Works as follows:

### `1.Floating Point Numbers Input Validation`:
It will prompt the user to enter the values of `a` and `b`. Anything the user will enter, it will be valid to create floating point numbers. If the user inputs something that isn't a number, it catches the `ValueError` and asks again.

### `2.Printing a Welcome Message`:
- This script, after taking the input values, prints out a centered, uppercase message, saying that a calculator is under development.

3. **Printing Options of Menu:**
   - The next things it does is provide a menu to the user for performing arithmetic operations like addition, subtraction, multiplication, exponentiation, division, floor division, and modulus.

4. **Validating the Input Provided for Menu Choice:
- Then, the script will prompt the user to enter a number between 1 and 7, which is supposed to select an operation. Besides that, it also provides input error checking and deals with whatever needs to be taken care of if the entered operation is not valid.

5. **Carry Out the Chosen Operation:**
   - Depending on the user's selection, this is where the script would then perform the chosen arithmetical operation:
- **Addition**: Returns the sum of `a` plus `b`.
- **Subtraction**: Returns `b` subtracted from `a`.
     - **Multiplication**: Multiply `a` with `b`
     - **Exponentiation**: Raises `a` to the power of `b`. If `b` is zero, it returns 1 since any number to the power of zero is 1.
- **Division:** This function divides a by b. In case of the division by zero, it prints an "undefined" message.
   - **Floor Division**: This performs the floor division of a by b. For division by zero again, it prints an "undefined" message.
   - **Modulus**: This calculates the remainder when a is divided by b.

6. **Special Operation Handling:
- Division and floor division: In case `b` is zero, it handles this special case of division by zero with an appropriate message.

7. **Check if Script is Run:**
   - The script has the standard `if __name__ == "__main__":` line inside which execution of code will take place.

This script is quite user-friendly in nature, as it neatly prompts the user, and common errors appear to have been handled in a smooth manner. Considering that the script performs basic arithmetic, the code is basic and functional.