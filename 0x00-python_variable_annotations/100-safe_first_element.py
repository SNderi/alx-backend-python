#!/usr/bin/env python3
""" Module to augment the code with
the correct duck-typed annotations.
"""

from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns first element of a list or none otherwise. """
    if lst:
        return lst[0]
    else:
        return None
