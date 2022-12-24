#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function that prints a dictionary by ordered keys."""
    for n in sorted(a_dictionary.items()):
        print(f"{n[0]}: {n[1]}")
