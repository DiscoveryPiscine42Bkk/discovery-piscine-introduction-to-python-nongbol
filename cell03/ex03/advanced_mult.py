#!/usr/bin/env python3

i = 0
while i <= 10:
    print("Table de " + str(i) + ":", end=" ")
    j = 0
    while j <= 10:
        print(str(i * j), end=" " if j < 10 else "")
        j += 1
    print()
    i += 1