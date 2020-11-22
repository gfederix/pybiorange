import numpy as np
import pytest

from bioranges.overlap import FindOverlaps
from bioranges.range import Range

def test_find_overlaps():
    r1 = Range(start=np.array([1, 4, 8]), end=np.array([2, 7, 10]))
    q1 = Range(start=np.array([3]), end=np.array([5]))

    for x in FindOverlaps(query=q1, subject=r1):
        pass
    overlapped = list(FindOverlaps(query=q1, subject=r1))
    assert len(overlapped) == 1
    assert overlapped == [Range(start=np.array([4]), end=np.array([7]))]
    assert (
        list(FindOverlaps(
            query=Range(
                start=np.array([8]),
                end=np.array([9])),
            subject=r1)) ==
        [Range(start=np.array([8]), end=np.array([10]))])
