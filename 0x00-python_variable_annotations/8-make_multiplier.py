#!/usr/bin/env python3
""" Module for a type-annotated function make_multiplier. """

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier.
    """
    return lambda x: multiplier * x
