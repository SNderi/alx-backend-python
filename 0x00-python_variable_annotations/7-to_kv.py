#!/usr/bin/env python3
""" Module for a type-annotated function to_kv. """

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple of k and the square of v
    """
    return (k, v * v)
