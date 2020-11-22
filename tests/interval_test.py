from bioranges.interval import Interval


# Tests Intervals
def test_interval():
    assert Interval(1, 10).contain(Interval(2, 8))
    assert not Interval(1, 10).contain(Interval(8, 11))
    assert Interval.Null().contain(Interval(10000,  100000000))
