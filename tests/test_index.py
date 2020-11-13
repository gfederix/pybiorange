import pytest

import numpy as np
from numpy.testing import assert_array_equal
from typing import List, Tuple, Iterable
from bioranges import RangeIndex
from bioranges.index import NCList, NCListBuilder, build_nclist, Intervals

# Utils & test for them
def start_end_from_zipped(
        it: Iterable[Tuple[int, int]]) -> Tuple[Tuple[int], Tuple[int]]:
    x = list(zip(*it))
    return map(np.array, x)


def test_start_end_from_zipped():
    s,e = start_end_from_zipped([(1, 10), (2, 20)])
    assert_array_equal(s, [1, 2])
    assert_array_equal(e, [10, 20])


# Tests
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
    assert NCList(1, [NCList(2)]) != NCList(1, [NCList(3)])
    assert NCList(1, [NCList(2, [NCList(3)])]) != NCList(1, [NCList(2, [NCList(4)])])

def test_counting_nc_list_on_modification_and_creation():
    ncl = NCList(None)
    ncl.append(NCList(1))
    assert len(ncl.childs) == 1
    assert len(ncl) == 1
    assert len(NCList(None, [NCList(1, [NCList(2)])])) == 2


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

# @pytest.mark.skip("enable after NCList compare will be done")
def test_building_nc_list_on_sorted_data():
    '''
      1 2 3 4 5 6 7 8 9 10 11
    0     -----
    1       -----
    2                 ---
    3              ------
    4     -------
      1 2 3 4 5 6 7 8 9 10 11
    '''
    r = [(3, 5), (4, 6), (9, 10), (8, 10), (3, 6)]
    idx = np.array([4, 0, 1, 3, 2], dtype=int)
    # nc = NCList(None)
    # assert build_nclist(np.array(r)[idx], lambda x, y: True) == NCList(None)
    s, e = start_end_from_zipped(r)
    ncb = NCListBuilder(Intervals(s, e))
    ncb.index = idx
    assert ncb._construct_nclist() == NCList(None, [NCList(4,[NCList(1), NCList(0)]), NCList(3,[NCList(2)])])
