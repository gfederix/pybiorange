import numpy as np
import pytest

from bioranges.overlap import FindOverlaps
from bioranges.range import Range


def test_empty_range():
    Range()


def test_range_with_ranges():
    r = Range(start=np.array([1, 2]), end=np.array([2, 3]))
    assert r.size() == 2


def test_range_stright_indexing():
    r = Range(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    assert r[0].size() == 1
    assert r[:2].size() == 2
    assert r[0:2].size() == 2
