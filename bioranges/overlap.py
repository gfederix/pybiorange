from array import array
from typing import Any

from bioranges.index import NCList
from bioranges.index import NCListBuilder
from bioranges.range import Range


class FindOverlaps:
    query: 'Range'
    subject: 'Range'
    index_builder: NCListBuilder  # TODO: make Interface by abstract class for AIListBuilder and NCListBuilder
    index: NCList                 # TODO: make Interface by abstract class for AIList and NCList

    def __init__(self, subject, index_builder=NCListBuilder):
        self.subject = subject
        # self.index_builder = index_builder
        self.index = self.build_index(subject.intervals, index_builder)

    def build_index(self, intervals, index_builder):
        return index_builder(intervals).build()

    def OVERLAPS_ANY(self, interval):  # TODO: probaly need move to intervals module ???
        return (
            lambda subject_idx:
            self.subject.intervals[subject_idx].start <= interval.end and
            interval.start <= self.subject.intervals[subject_idx].end)

    def query(self, query):
        for i in query.intervals:
            idx_iter = self.index.find_overlap_index(self.OVERLAPS_ANY(i))
            yield self.subject[array('i', idx_iter)]
