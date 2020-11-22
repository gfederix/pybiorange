from typing import Callable
from typing import Iterable
from typing import List
from typing import Tuple

import numpy as np


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
        # TODO: move to NCList builder. While it's NCList specific sorting
        idx = sorted(
            self.index,
            key=lambda i: NCListCMP(self.start, self.end, i))
        self.index = np.array(idx, dtype=int)


class NCList:
    '''
    Algorithm from
    Nested Containment List (NCList): a new algorithm for accelerating interval
    query of genome alignment and interval databases

    Authors: Alexander V. Alekseyenko and Christopher J. Lee

    doi: https://dx.doi.org/10.1093/bioinformatics/btl647

    Unfortunately no supplementary data available. So I have no pseudocode of
    building NCList algorithm which in supplementary.
    '''
    def __init__(self, value, childs=None):
        self.childs_count = 0
        self.value = value
        self.childs = [] if childs is None else childs
        for c in self.childs:
            self.childs_count += 1 + c.childs_count

    def __repr__(self):
        if len(self.childs) == 0:
            return f'NCList({self.value})'
        else:
            child_repr_str = ', '.join(map(repr, self.childs))
            return f'NCList({self.value}, [{child_repr_str}])'

    def __eq__(self, other):
        # TODO: unwind recursion someday
        if not hasattr(other, 'value'):
            return self.value == other
        childs = self.childs
        other_childs = other.childs
        if self.value != other.value:
            return False
        if len(self.childs) != len(other.childs):
            return False
        for i in range(len(childs)):
            if childs[i] != other_childs[i]:
                return False
        return True

    def __iter__(self) -> Iterable['NCList']:
        yield from self.childs

    def append(self, x: 'NCList'):
        self.childs.append(x)
        self.childs_count += 1 + x.childs_count

    def __len__(self):
        return self.childs_count

    def find_overlap_index(
            self,
            is_overlap: Callable[[int], bool]) -> Iterable[int]:
        # TODO: make binary search instead iteration within childrens list!!!!
        # TODO: move to another class. Probably to RangeIndex. While it's
        # probably more common function. And shuld be usable with AIList...
        childs_of_intersected = [self.childs]
        while len(childs_of_intersected) != 0:
            childs = childs_of_intersected.pop()
            for c in childs:
                if is_overlap(c.value):
                    yield c.value
                    if len(c.childs) != 0:
                        childs_of_intersected.append(c.childs)


class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'Interval({self.start}, {self.end})'

    def contain(self, other):
        return self.start <= other.start and other.end <= self.end

    class Null:
        def contain(self, other):
            return True


class Intervals:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __getitem__(self, i):
        return Interval(self.start[i], self.end[i])


class NCListBuilder:
    def __init__(self, intervals):
        self.intervals = intervals
        self.index = np.array([], dtype=int)

    def _construct_nclist_from_sorted_index(self):
        root = NCList(None)
        nclist_pointers = []
        for i in self.index:
            cur_interval = self.intervals[i]
            cur_nclist = NCList(i)
            while len(nclist_pointers) != 0:
                prev_nclist = nclist_pointers[len(nclist_pointers) - 1]
                prev_int = self._get_nclist_interval(prev_nclist)
                if prev_int.contain(cur_interval):
                    prev_nclist.append(cur_nclist)
                    break
                nclist_pointers.pop()
            else:
                root.append(cur_nclist)
            nclist_pointers.append(cur_nclist)
        return root

    def _get_nclist_interval(self, nclist: NCList):
        return self.intervals[nclist.value]


class AIList:
    '''
    Augmented Interval List: a novel data structure for efficient genomic
    interval search

    Authors: Jianglin Feng, Aakrosh Ratan, and Nathan C. Sheffield

    doi: https://dx.doi.org/10.1101/593657
    '''
    pass
