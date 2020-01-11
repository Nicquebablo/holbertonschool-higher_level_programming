#!/usr/bin/python3


"""Integer addition"""

def add_integer(a, b=98):
    """
    Function adds two integers
    """
    try:
        return int(a) + (b)
    except:
        if isinstance(a, int) is False or isinstance(a, float) is False:
            raise TypeError ('a must be an integer')
        if (isinstance(b, int) is False) or (isinstance(b, float) is False):
            raise TypeError ('b must be an integer')
