#!/usr/bin/env python3
""" Module for annotating the a function’s parameters
and return values with the appropriate types.
"""

from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
