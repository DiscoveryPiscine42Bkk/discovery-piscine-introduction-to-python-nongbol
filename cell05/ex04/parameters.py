#!/usr/bin/env python3

import sys

def main():
    # sys.argv[0] is the script name, so parameters start from index 1
    param_count = len(sys.argv) - 1
    print(f"Number of parameters: {param_count}.")

if __name__ == "__main__":
    main()
