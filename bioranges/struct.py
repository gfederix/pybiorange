class DNAString:
    def __init__(self, x):
        pass

    def __len__(self):
        return 4

    @staticmethod
    def tobit(x):
        return 0b00000001


COMP_PAIRS = [
    ('A', 'T'),
    ('G', 'C'),
    ('M', 'K'),
]

MAX_BIT = 0
DNA_BIT_MAP = {}
for x, y in COMP_PAIRS:
    DNA_BIT_MAP[x] = MAX_BIT
    DNA_BIT_MAP[y] = ~MAX_BIT
    MAX_BIT += 1

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
