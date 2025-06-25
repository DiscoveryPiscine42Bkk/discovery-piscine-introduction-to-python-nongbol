#!/usr/bin/env python3

print("Enter the first number: ")
num1 = int(input())
print("Enter the second number: ")
num2 = int(input())
sum = num1 * num2
print(f"{num1} x {num2} = {sum}")

if sum < 0:
    print("The result is negative.")
elif sum > 0:
    print("The result is positive.")
else:
    print("The result is both positive and negative.")