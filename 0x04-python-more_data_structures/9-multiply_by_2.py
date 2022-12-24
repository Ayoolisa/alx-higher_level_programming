#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({n: a_dictionary[n] * 2 for n in a_dictionary})
