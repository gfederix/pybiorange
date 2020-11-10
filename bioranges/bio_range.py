import numpy as np


class BioRange:
    def __init__(self, start=None, end=None):
        if start is None or end is None:
            return
        self.start = start
        self.end = end

    def size(self):
        return len(self.start)

    def __getitem__(self, key):
        start = self.start.__getitem__(key)
        end = self.end.__getitem__(key)
        if type(key) is int:
            start = np.array([start])
            end = np.array([end])
        return BioRange(start=start, end=end)
