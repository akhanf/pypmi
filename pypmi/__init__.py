# -*- coding: utf-8 -*-

__all__ = [
    '__author__', '__description__', '__email__', '__license__',
    '__maintainer__', '__packagename__', '__url__', '__version__',
    'datasets', 'bids', 'misc', 'pivot', 'get_studydata',
]

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .info import (
    __author__,
    __description__,
    __email__,
    __license__,
    __maintainer__,
    __packagename__,
    __url__,
)

from .datasets import get_studydata as get_studydata
from . import bids, misc, pivot
