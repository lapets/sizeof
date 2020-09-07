"""Function for measuring memory usage of objects.

Simple function for measuring the size in memory of
common Python data structures.
"""

from __future__ import annotations
import doctest
import sys
import collections

def sizeof(obj, deep=False, _exclude=None):
    """
    Estimate the memory consumption of a Python object (either
    the root object itself exclusively or, in the case of a deep
    traversal, the entire tree of objects reachable from it).
    """
    if not deep or isinstance(obj, (str, bytes, bytearray, int, float)):
        return sys.getsizeof(obj)

    _exclude = set() if _exclude is None else _exclude

    if id(obj) in _exclude:
        return 0

    if isinstance(obj, collections.abc.Mapping):
        iterator = obj.items() if isinstance(obj, dict) else obj.iteritems()
        return sys.getsizeof(obj) + sum(
            sizeof(k, deep=True, _exclude=_exclude.union({id(obj)})) +\
            sizeof(v, deep=True, _exclude=_exclude.union({id(obj)}))
            for (k, v) in iterator
        )

    if isinstance(obj, collections.abc.Container):
        return sys.getsizeof(obj) + sum(
            sizeof(v, deep=True, _exclude=_exclude.union({id(obj)}))
            for v in obj
        )

    raise ValueError(
        'object not supported by current version of sizeof'
    )

if __name__ == "__main__":
    doctest.testmod()
