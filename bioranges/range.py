from typing import Dict
from typing import Optional

import numpy as np
from nptyping import NDArray

from bioranges.interval import Intervals
from bioranges.show_table import RowPresenter


class NullRange:
    def size(self):
        return 0

    def __getitem__(self, key):
        raise IndexError


class Range:
    intervals: Intervals
    Null = NullRange()

    def __init__(
            self,
            start: Optional[NDArray[int]] = None,
            end: Optional[NDArray[int]] = None,
            data: Optional[Dict] = None):
        if start is None or end is None:
            return
        self.intervals = Intervals(start=start, end=end)

    def size(self):
        return len(self.intervals)

    def __eq__(self, other):
        if type(other) is NullRange:
            return False
        return self.intervals == other.intervals

    def __getitem__(self, key):
        start = self.intervals.start.__getitem__(key)
        end = self.intervals.end.__getitem__(key)
        if type(key) is int:
            start = np.array([start])
            end = np.array([end])
        return Range(start=start, end=end)

    def __repr__(self):
        return '\n'.join(
            RowPresenter(name='Interval', type='int', data=self.intervals))
