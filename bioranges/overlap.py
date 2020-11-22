from typing import Any

from bioranges.bio_range import Range
from bioranges.index import NCList
from bioranges.index import NCListBuilder

class FindOverlaps:
    query: 'Range'
    subject: 'Range'
    index_builder: NCListBuilder  # TODO: make Interface by abstract class for AIListBuilder and NCListBuilder
    index: NCList                 # TODO: make Interface by abstract class for AIList and NCList
    def __init__(self, query, subject, index_builder=NCListBuilder):
        self.query = query
        self.subject = subject
        self.index_builder = index_builder

    def __iter__(self):
        yield from [self.subject[2]]
