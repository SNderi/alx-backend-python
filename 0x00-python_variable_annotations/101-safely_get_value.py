#!/usr/bin/env python3
""" Module to add type annotations to a function. """

from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Returns a dict value or none otherwise. """
    if key in dct:
        return dct[key]
    else:
        return default
