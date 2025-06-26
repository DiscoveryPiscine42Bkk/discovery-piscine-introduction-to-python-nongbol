#!/usr/bin/env python3

import math

def main():
    user_input = input("Give me a number: ")
    try:
        number = float(user_input)
    except ValueError:
        print("That's not a valid number.")
        return

    rounded_up = math.ceil(number)
    print(rounded_up)

if __name__ == "__main__":
    main()
