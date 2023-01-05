#!/usr/bin/env python3
""" Module to validate a piece of code using mypy. """

from typing import List, Tuple, Union, Any


def zoom_array(lst: List, factor: Any = 2) -> List:
    """ Returns a list zoomed in by a factor. """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
