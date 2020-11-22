from typing import Dict
from typing import Optional

import numpy as np
from nptyping import NDArray


class NullRange:
    def size(self):
        return 0

    def __getitem__(self, key):
        raise IndexError


class Range:
    start: NDArray[int]
    end: NDArray[int]
    Null = NullRange()

    def __init__(
            self,
            start: Optional[NDArray[int]] = None,
            end: Optional[NDArray[int]] = None,
            data: Optional[Dict] = None):
        if start is None or end is None:
            return
        self.start = start
        self.end = end

    def size(self):
        return len(self.start)

    def __getitem__(self, key):
        start = self.start.__getitem__(key)
        end = self.end.__getitem__(key)
        if type(key) is int:
            start = np.array([start])
            end = np.array([end])
        return Range(start=start, end=end)
