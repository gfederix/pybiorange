import numpy as np
import pytest

from bioranges.range import Range


def test_empty_range():
    Range()


def test_range_with_ranges():
    r = Range(start=np.array([1, 2]), end=np.array([2, 3]))
    assert r.size() == 2


def test_rowclass():
    r = Range(
        start=np.array([1, 2]),
        end=np.array([2, 3]),
        data={'aa': [1, 5], 'bb': [8, 9]}
    )
    row = r.Row(*[1, 3])
    assert row.aa == 1
    assert row.bb == 3


def test_iterate_over_row():
    r0 = Range(start=np.array([1, 2]), end=np.array([2, 3]))
    assert len(list(r0.iterrows())) == 0
    r1 = Range(
        start=np.array([1, 2]),
        end=np.array([2, 3]),
        data={'aa': [1, 5], 'bb': [8, 9]}
    )
    assert len(list(r1.iterrows())) == 2
    r1_iter = iter(r1.iterrows())
    r10 = next(r1_iter)
    assert r10.aa == 1 and r10.bb == 8
    r11 = next(r1_iter)
    assert r11.aa == 5 and r11.bb == 9


def test_range_stright_indexing():
    r = Range(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    assert r[0].size() == 1
    assert r[:2].size() == 2
    assert r[0:2].size() == 2


def test_null_range_object():
    r1 = Range(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    assert r1 != Range.Null
    assert r1 != Range.Null


def test_range_repr():
    r1 = Range(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    assert (r1.__repr__() ==
            ' Intervals\n<Interval>\n       1-2\n       2-3\n       3-4')


def test_range_equality():
    r1 = Range(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    r2 = Range(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    r3 = Range(start=np.array([100,]), end=np.array([200]))
    assert r1 == r2
    assert r1 != r3
