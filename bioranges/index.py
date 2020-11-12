import numpy as np
from typing import List, Iterable, Callable

class NCListCMP:
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
            self.start[self.i] > other.start[other.i]
            or (self.start[self.i] == other.start[other.i]
                and self.end[self.i] < other.end[other.i]))


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
        idx = sorted(
            self.index,
            key=lambda i: NCListCMP(self.start, self.end, i))
        self.index = np.array(idx, dtype=int)


class NCList:
    def __init__(self, value, childs=None):
        if childs is None:
            self.childs = []
        else:
            self.childs = childs
        self.value = value

    def __eq__(self, other):
        try:
            return self.value == other.value
        except AttributeError:
            return self.value == other

    def __iter__(self):
        for child in self.childs:
            yield child

    def find_overlap_index(
            self,
            is_overlap: Callable[[int], bool]) -> Iterable[int]:
        # TODO: make binary search instead iteration within childrens list!!!!
        childs_of_intersected = [self.childs]
        while len(childs_of_intersected) != 0:
            childs = childs_of_intersected.pop()
            for c in childs:
                if is_overlap(c.value):
                    yield c.value
                    if len(c.childs):
                        childs_of_intersected += [c.childs]
