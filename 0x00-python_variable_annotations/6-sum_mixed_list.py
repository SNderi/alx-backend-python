#!/usr/bin/env python3
""" Module for a type-annotated function sum_mixed_list. """

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Adds up a list of integers and floats
    Return:
        Sum (float)
    """
    return sum(mxd_lst)
