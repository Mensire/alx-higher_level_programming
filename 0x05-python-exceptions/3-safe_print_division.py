#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = 0.0
        c = a / b
        return c
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
        return None
    finally:
            print("Inside result: {:d}".format(c))
