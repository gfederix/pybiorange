import numpy as np

from bioranges.interval import Interval
from bioranges.interval import Intervals


# Tests Intervals
def test_interval():
    assert Interval(1, 10).contain(Interval(2, 8))
    assert not Interval(1, 10).contain(Interval(8, 11))
    assert Interval.Null.contain(Interval(10000,  100000000))


def test_interval_equality():
    assert Interval(1, 10) == Interval(1, 10)
    assert Interval(1, 10) != Interval(1, 1)


def test_intervals_equality():
    assert (Intervals(start=np.array([1, 2]), end=np.array([10, 20])) ==
            Intervals(start=np.array([1, 2]), end=np.array([10, 20])))
    assert (Intervals(start=np.array([1, 2]), end=np.array([10, 20])) !=
            Intervals(start=np.array([1]), end=np.array([10])))

def test_intervals_repr():
    assert Interval(start=1, end=2).__repr__() == 'Interval(1, 2)'
    assert (Intervals(start=np.array([1, 10]), end=np.array([2, 15])).__repr__() ==
            'Intervals:\n1-2\n10-15\n')
