from unittest.mock import mock_open
from unittest.mock import patch

import pytest

from bioranges.io import read_bed


@pytest.fixture()
def bedgraph_file(mocker):
    """
    https://m.ensembl.org/info/website/upload/bed.html
    https://genome.ucsc.edu/goldenPath/help/customTrack.html
    https://genome.ucsc.edu/goldenPath/help/bedgraph.html
    """
    bedgraph_file = """\
browser position chr19:49302001-49304701
browser hide all
browser pack refGene encodeRegions
browser full altGraph
#	300 base wide bar graph, autoScale is on by default == graphing
#	limits will dynamically change to always show full range of data
#	in viewing window, priority = 20 positions this as the second graph
#	Note, zero-relative, half-open coordinate system in use for bedGraph format
track type=bedGraph name="BedGraph Format" description="BedGraph format" visibility=full color=200,100,0 altColor=0,100,200 priority=20
chr19 49302000 49302300 -1.0
chr19 49302300 49302600 -0.75
chr19 49302600 49302900 -0.50
chr19 49302900 49303200 -0.25
chr19 49303200 49303500 0.0
chr19 49303500 49303800 0.25
chr19 49303800 49304100 0.50
chr19 49304100 49304400 0.75
chr19 49304400 49304700 1.00
"""
    mocker.patch('builtins.open', mock_open(read_data=bedgraph_file))
    yield 'bedgraph_file'


@pytest.fixture
def wig_file():
    """
    https://genome.ucsc.edu/goldenPath/help/wiggle.html
    """
    pass


@pytest.fixture
def bed_file():
    """
    https://genome.ucsc.edu/FAQ/FAQformat.html#format1
    """
    pass


def test_bedgraph_read(bedgraph_file):
    bed = read_bed(bedgraph_file)
    assert bed.track.name == 'BedGraph Format'
