#!/usr/bin/env python3

def main():
    try:
        num1 = float(input("Give me the first number: "))
        num2 = float(input("Give me the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("Thank you!")
    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print(f"{num1} / {num2} = Error (division by zero)")
    print(f"{num1} * {num2} = {num1 * num2}")

if __name__ == "__main__":
    main()
