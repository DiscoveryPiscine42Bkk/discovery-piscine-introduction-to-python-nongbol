#!/usr/bin/env python3

def main():
    age_input = input("Please tell me your age: ")
    try:
        age = int(age_input)  # Convert string to integer
    except ValueError:
        print("That doesn't look like a valid number.")
        return

    print(f"You are currently {age} years old.")
    print(f"In 10 years, you'll be {age + 10} years old.")
    print(f"In 20 years, you'll be {age + 20} years old.")
    print(f"In 30 years, you'll be {age + 30} years old.")

if __name__ == "__main__":
    main()