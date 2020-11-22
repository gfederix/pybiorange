from bioranges.range import Range
from bioranges.utils import rbind

def test_range_concat():
    r1 = Range.Null
    r2 = Range.Null
    assert rbind(r1, r2) == Range.Null
