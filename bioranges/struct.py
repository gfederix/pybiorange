from abc import ABC
from abc import abstractmethod
from typing import Iterable
from typing import List
from typing import Optional
from typing import Union

import numpy as np
from nptyping import NDArray
# from collections import Iterable

IUPAC_CODE_MAP = {
    'A': 'A',
    'C': 'C',
    'G': 'G',
    'T': 'T',
    'M': 'AC',
    'R': 'AG',
    'W': 'AT',
    'S': 'CG',
    'Y': 'CT',
    'K': 'GT',
    'V': 'ACG',
    'H': 'ACT',
    'D': 'AGT',
    'B': 'CGT',
    'N': 'ACGT'
}

DNA_CHAR_ARRAY = np.array([     # ..CTGA
    '-',                        # 0b0000 -
    'A',                        # 0b0001 A
    'G',                        # 0b0010 G
    'R',                        # 0b0011 GA == puRine
    'T',                        # 0b0100 T
    'W',                        # 0b0101 TA == Weak
    'K',                        # 0b0110 TG == Keto
    'D',                        # 0b0111 TGA == Not C -> D
    'C',                        # 0b1000 C
    'M',                        # 0b1001 CA == aMino
    'S',                        # 0b1010 CG == Strong
    'V',                        # 0b1011 CGA == Not T -> V
    'Y',                        # 0b1100 TC == pYrimidine
    'H',                        # 0b1101 TCA == Not G -> H
    'B',                        # 0b1110 CTG == Not A -> B
    'N',                        # 0b1111 TCGA = aNy
])

DNA_CHAR_TO_BIT_MAP = {char: val for val, char in enumerate(DNA_CHAR_ARRAY)}


def complement(x: Union[int, NDArray[np.int8]]):
    return x >> 2 | (x & 0b00110011) << 2


def complement4(x: Union[int, NDArray[np.int8]]):
    """Four bit complement for 2 nucleotide packed in 8bit"""
    return (x & 0b11001100) >> 2 | (x & 0b00110011) << 2


class DNAStr:
    data: Optional[NDArray[np.int8]]

    def __init__(self, x: Optional[str] = None):
        if isinstance(x, str):
            self.init_from_string(x)
        elif isinstance(x, np.ndarray):
            self.data = x
        else:
            self.data = np.array([], dtype=np.int8)

    def init_from_string(self, x: str):
        self.data = np.array(
            [DNA_CHAR_TO_BIT_MAP[c] for c in x], dtype=np.int8)

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return ''.join(DNA_CHAR_ARRAY[x] for x in self.data)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    @staticmethod
    def tobit(x: str):
        return 0b00000001

    def complement(self):
        cls = type(self)
        nt = self.data >> 2 | (self.data << 2 & 0b1100)
        return cls(nt)


class Vec(ABC):                 # TODO: move to Range
    @abstractmethod
    def resize(self):
        pass


class DNAVec(Vec):
    data: List[Optional[NDArray[np.int8]]]

    def __init__(
            self,
            x: Union[Iterable[str], List[NDArray[np.int8]], None] = None):
        if isinstance(x, List):
            self.data = x
        elif isinstance(x, Iterable):
            self.data = [self.array_from_str(string) for string in x]
        else:
            self.data = []

    def array_from_str(self, x: str):
        return np.array([DNA_CHAR_TO_BIT_MAP[c] for c in x], dtype=np.int8)

    def __iter__(self) -> Iterable[Optional[DNAStr]]:
        # TODO: Return somthing like DNAstr.NA instead None? Or do not use
        # DNAStr at all and DNAVec[1] will bee enought?
        for x in self.data:
            if x is None:
                yield None
            else:
                yield DNAStr(x)

    def resize(self, x):
        data = [nt[:x] if len(nt) >= x else None for nt in self.data]
        return DNAVec(data)
