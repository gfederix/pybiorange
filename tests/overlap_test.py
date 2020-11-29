import numpy as np
import pytest

from bioranges.index import NCList
from bioranges.overlap import FindOverlaps
from bioranges.range import Range


def test_find_overlaps():
    r1 = Range(start=np.array([1, 4, 8]), end=np.array([2, 7, 10]))
    q1 = Range(start=np.array([3]), end=np.array([5]))
    fo = FindOverlaps(subject=r1)
    assert fo.index == NCList(None, [NCList(0), NCList(1), NCList(2)])
    for x in fo.query(query=q1):
        pass
    overlapped = list(fo.query(query=q1))
    assert len(overlapped) == 1
    assert overlapped == [Range(start=np.array([4]), end=np.array([7]))]


def test_find_complex_overlaps():
    r1 = Range(start=np.array([1, 4, 8]), end=np.array([2, 7, 10]))
    fo = FindOverlaps(subject=r1)
    assert (
        list(fo.query(
            Range(
                start=np.array([8]),
                end=np.array([9])),)) ==
        [Range(start=np.array([8]), end=np.array([10]))]
    )

    assert (
        list(fo.query(
            Range(
                start=np.array([4]),
                end=np.array([9])),)) ==
        [Range(start=np.array([4, 8]), end=np.array([7, 10]))]
    )

    assert (
        list(fo.query(
            Range(
                start=np.array([1, 8]),
                end=np.array([1, 8])),)) ==
        [Range(start=np.array([1]), end=np.array([2])),
         Range(start=np.array([8]), end=np.array([10]))]
    )
