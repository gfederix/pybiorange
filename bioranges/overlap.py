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
        self.index_builder = index_builder

    def query(self, query):
        yield from [self.subject[1]]
