#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """returns a new list length
    if element is not an integer or float it prints wrong type
    zeroerror print division by zero
    if both lists are too short print out of range
"""
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i]/my_list_2[i]
            div = 0
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(div)
    return(new_list)

