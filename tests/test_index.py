import pytest

import numpy as np
from numpy.testing import assert_array_equal

from bioranges import RangeIndex
from bioranges.index import NCList


def test_range_index_for_sorted_non_intersected_ranges():
    idx = RangeIndex(start=np.array([1, 10]), end=np.array([2, 20]))
    assert_array_equal(idx.index, [0, 1])


def test_range_index_for_unsorted_non_intersected_ranges():
    idx = RangeIndex(start=np.array([10, 1]), end=np.array([20, 2]))
    assert_array_equal(idx.index, [1, 0])


def test_range_index_for_unsorted_nested_ranges():
    idx = RangeIndex(
        #                0   1   2  3
        start=np.array([10,  1,  4, 3]),
        end=np.array(  [20, 10, 11, 4]))
    assert_array_equal(idx.index, [1, 3, 2, 0])

    idx2 = RangeIndex(
        #                0   1   2  3
        start=np.array([10,  1,  4, 4]),
        end=np.array(  [20, 10, 11, 10]))
    assert_array_equal(idx2.index, [1, 2, 3, 0])


def test_empty_nclist():
    NCList(0)


def test_nonempty_nclist():
    ncl = NCList(None, [NCList(1), NCList(2), NCList(3)])
    assert list(ncl) == [1, 2, 3]


def test_nc_list_equality():
    assert NCList(1) == NCList(1)
    assert NCList(1) != NCList(2)


@pytest.mark.skip(
    "Not shure about this."
    "Probably i need use __len__() instead child."
    "Shuld I count all neasted childs or just nearest childs?")
def test_nc_list_child_interfaces():
    assert NCList(None).childs() == 0


def test_search_in_builded_nc_list():
    #      0       0->1  0->0  0     1     1      1
    #      0       1     2     3     4     5      6
    a = [False, True, True,  False, True, True, False]
    nc = NCList(None, [
        NCList(0),
        NCList(1, [NCList(4), NCList(5), NCList(6)]),
        NCList(2),
        NCList(3)])
    assert list(nc.find_overlap_index(lambda i: a[i])) == [1, 2, 4, 5]
