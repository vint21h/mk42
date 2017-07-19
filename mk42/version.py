# -*- coding: utf-8 -*-

# mk42
# mk42/version.py

from __future__ import unicode_literals
from datetime import date


__all__ = [
    "VERSION",
    "__version__",
    "__updated__",
]


# project start date: 12.06.2017
# project last update date: 19.07.2017


VERSION = (0, 0, 0)
__version__ = ".".join(map(str, VERSION))
__updated__ = date(2017, 7, 19)
