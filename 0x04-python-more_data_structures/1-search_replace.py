#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
        a function that replaces all
        occurrences of an element by
        another in a new list.

        my_list - the initial list
        search - the element to be replaced
        replace - the new element
    """
    new_list = my_list[:]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return (new_list)
