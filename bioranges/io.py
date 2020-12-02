from abc import ABC
from abc import abstractmethod
from collections import namedtuple

TrackLine = namedtuple('TrackLine', ['name'])


# TODO: here probably need create adaptor class for init: Range(BadFile(file)),
# Range(Dict({})), Range(WigFile())
class ReadFile(ABC):
    @abstractmethod
    def trackline() -> TrackLine:
        pass


class RangeAdapter(ABC):        # TODO: to acess SQL and etc
    @abstractmethod
    def trackline() -> TrackLine:
        pass


class FackedRange:
    def __init__(self):
        self.track = TrackLine(name='BedGraph Format')


def read_bed(file):
    return FackedRange()
