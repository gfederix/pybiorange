import pytest

import numpy as np
from numpy.testing import assert_array_equal

from bioranges import RangeIndex


def test_range_index_for_sorted_non_intersected_ranges():
    idx = RangeIndex(start=np.array([1, 10]), end=np.array([2, 20]))
    assert_array_equal(idx.index, [0, 1])


def test_range_index_for_unsorted_non_intersected_ranges():
    idx = RangeIndex(start=np.array([10, 1]), end=np.array([20, 2]))
    assert_array_equal(idx.index, [1, 0])

def test_range_index_for_unsorted_intersected_ranges():
    idx = RangeIndex(
        #                0   1   2  3
        start=np.array([10,  1,  2, 3]),
        end=np.array(  [20, 10, 11, 4]))
    assert_array_equal(idx.index, [1, 3, 2, 0])
