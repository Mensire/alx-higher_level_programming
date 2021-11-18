#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum of a and b."""
    def add(a, b):
        a = 2
        b = 3
        print("{} + {} = {}".format(a, b, add(a, b)))
