from typing import Union

from nptyping import NDArray


class Interval:
    start: int
    end: int

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'Interval({self.start}, {self.end})'

    def contain(self, other: 'Interval'):
        return self.start <= other.start and other.end <= self.end

    class Null:
        def contain(self, other: 'Interval'):
            return True


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
