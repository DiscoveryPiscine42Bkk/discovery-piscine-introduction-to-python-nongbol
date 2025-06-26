#!/usr/bin/env python3

def main():
    user_input = input("Give me a number: ")
    try:
        number = float(user_input)  # string to float conversion
    except ValueError:
        print("That's not a valid number.")
        return

    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")

if __name__ == "__main__":
    main()
