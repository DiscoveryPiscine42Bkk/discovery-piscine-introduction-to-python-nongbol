#!/usr/bin/env python3

import sys

def main():
    params = sys.argv[1:]
    if len(params) < 2:
        print("none")
    else:
        for p in reversed(params):
            print(p)

if __name__ == "__main__":
    main()
