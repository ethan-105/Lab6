"""
Lab6.py
Created by Ethan Pena, who wrote encode() and main(), as well as the initializing condition.
The Decoder will be written by someone else.
Last updated on 3/7/2023.
"""

# Global variables start here.

encoded_pass = ""


# Functions start here.

# Encodes password so each digit is 3 higher (or if over 10, 3 higher and 10 down).
def encode(password):
    new_pass = ""
    for char in password:
        new_pass += str((int(char) + 3) % 10)

    return new_pass


# Decodes passed value to initial value.
def decode(arg):
    newstring = ''
    for x in arg:
        newstring += str((int(x) - 3) % 10)
    return newstring
    pass  # Replace with your code, partner! Please return the decoded password!


# Prints the entire menu.
def print_menu():
    print("Menu\n"
          "-------------\n"
          "1. Encode\n"
          "2. Decode\n"
          "3. Quit\n")


# Runs the loop, prints the menu, handles inputs, and calls other functions above.
def main():
    global encoded_pass
    while True:
        print_menu()
        option = int(input("Please enter an option: "))
        if option == 1:
            encoded_pass = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.\n")
        elif option == 3:  # Could be 'else', depends on tests.
            quit()


# Only runs main if the file is explicitly ran.
if __name__ == "__main__":
    main()
