"""
Lab6.py
Created by Ethan Pena, who wrote encode() and main(), as well as the initializing condition.
The Decoder will be written by someone else.
Last updated on 3/7/2023.
"""

# Globals go here.

encoded_pass = ""

# Functions start here.


def encode(password):
    new_pass = ""
    for char in password:
        new_pass += str((int(char) + 3) % 10)

    return new_pass


def decode(*args):
    pass


def print_menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")


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


if __name__ == "__main__":
    main()
