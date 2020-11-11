import numpy as np


class Cmp:
    def __init__(self, start, end, i):
        self.start = start
        self.end = end
        self.i = i

    def __eq__(self, other):
        return (
            self.start[self.i] == other.start[other.i]
            and self.end[self.i] == other.end[other.i])

    def __gt__(self, other):
        return (
            self.start[self.i] > other.end[other.i]
            or self.start[self.i] > other.start[other.i])


class RangeIndex:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.size = len(start)
        self.index = self._build_index()
        self._sort_index()

    def _build_index(self):
        idx = np.empty(self.size, dtype=int)
        for i in range(self.size):
            idx[i] = i
        return idx

    def _sort_index(self):
        # idx = sorted(self.index, key=lambda i: self.start[i])
        idx = sorted(self.index, key=lambda i: Cmp(self.start, self.end, i))
        self.index = np.array(idx, dtype=int)
