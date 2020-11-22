from typing import Union

import numpy as np
from nptyping import NDArray


class NullInterval:
    def contain(self, other: 'Interval'):
        return True


class Interval:
    start: int
    end: int
    Null = NullInterval()

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'Interval({self.start}, {self.end})'

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def contain(self, other: 'Interval'):
        return self.start <= other.start and other.end <= self.end


class Intervals:
    start: NDArray[int]
    end: NDArray[int]

    def __init__(self, start: NDArray[int], end: NDArray[int]):
        self.start = start
        self.end = end

    def __getitem__(self, i: Union[int, slice]):
        return Interval(self.start[i], self.end[i])

    def __len__(self):
        return len(self.start)

    def __eq__(self, other):
        return np.array_equal(self.start, other.start) and np.array_equal(self.end, other.end)
