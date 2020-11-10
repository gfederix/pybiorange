import numpy as np


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
        idx = sorted(self.index, key=lambda i: self.start[i])
        self.index = np.array(idx, dtype=int)
