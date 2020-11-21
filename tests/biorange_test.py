import numpy as np
import pytest

from bioranges import BioRange


def test_empty_biorange():
    BioRange()


def test_biorange_with_ranges():
    r = BioRange(start=np.array([1, 2]), end=np.array([2, 3]))
    assert r.size() == 2


def test_biorange_stright_indexing():
    r = BioRange(start=np.array([1, 2, 3]), end=np.array([2, 3, 4]))
    assert r[0].size() == 1
    assert r[:2].size() == 2
    assert r[0:2].size() == 2
