#!/usr/bin/env python3

num = int(input("Enter a number:\n"))
mult = int(0)

while mult <= num:
    sum = mult * num
    print(f"{mult} x {num} = {sum}")
    mult += 1