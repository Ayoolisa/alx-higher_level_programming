#!/usr/bin/python3


"""Defines a JSON-to-object function."""
import json


def to_json_string(my_obj):
    """Return the Python object representation of a JSON string."""
    return json.dumps(my_obj)
