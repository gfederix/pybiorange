import numpy as np

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


def complement(x):
    return x >> 2 | (x << 2 & 0b1100)


class DNAString:
    def __init__(self, x):
        self.data = np.array([DNA_CHAR_TO_BIT_MAP[c] for c in x])

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return ''.join(DNA_CHAR_ARRAY[x] for x in self.data)

    def __eq__(self, other):
        return np.array_equal(self.data, other.data)

    @staticmethod
    def tobit(x):
        return 0b00000001