from collections import namedtuple


TrackLine = namedtuple('TrackLine', ['name'])


class FackedRange:
    def __init__(self):
        self.track = TrackLine(name='BedGraph Format')


def read_bed(file):
    return FackedRange()
