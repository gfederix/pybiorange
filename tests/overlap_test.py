import numpy as np
import pytest

from bioranges.overlap import FindOverlaps
from bioranges.range import Range

def test_find_overlaps():
    r1 = Range(start=np.array([3]), end=np.array([5]))
    r2 = Range(start=np.array([1, 4, 8]), end=np.array([2, 7, 10]))
    for x in FindOverlaps(query=r1, subject=r2):
        pass
    overlapped = list(FindOverlaps(query=r1, subject=r2))
    assert len(overlapped) == 1
