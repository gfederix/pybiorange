import pytest

from bioranges.struct import complement
from bioranges.struct import DNA_CHAR_TO_BIT_MAP
from bioranges.struct import DNAString


def test_dna_string():
    dna = DNAString('ATGC')
    assert len(dna) == 4


def test_dna_string_compare():
    assert DNAString('ATGC') == DNAString('ATGC')


def test_dna_string_repr():
    assert DNAString('ATGC').__repr__() == 'ATGC'


def test_binarization():
    DNAString.tobit('A') == 0b1


def test_complementaryity_in_binarization():
    # DNAString.tobit("A") == 0b1
    # DNAString.tobit("T") == 0b1
    assert DNA_CHAR_TO_BIT_MAP['A'] == complement(DNA_CHAR_TO_BIT_MAP['T'])
    assert DNA_CHAR_TO_BIT_MAP['G'] == complement(DNA_CHAR_TO_BIT_MAP['C'])
    assert DNA_CHAR_TO_BIT_MAP['A'] != DNA_CHAR_TO_BIT_MAP['G']

    assert DNA_CHAR_TO_BIT_MAP['W'] == complement(DNA_CHAR_TO_BIT_MAP['W'])
    assert DNA_CHAR_TO_BIT_MAP['S'] == complement(DNA_CHAR_TO_BIT_MAP['S'])
    assert DNA_CHAR_TO_BIT_MAP['M'] == complement(DNA_CHAR_TO_BIT_MAP['K'])
    assert DNA_CHAR_TO_BIT_MAP['K'] == complement(DNA_CHAR_TO_BIT_MAP['M'])
    assert DNA_CHAR_TO_BIT_MAP['N'] == complement(DNA_CHAR_TO_BIT_MAP['N'])
    assert DNA_CHAR_TO_BIT_MAP['-'] == complement(DNA_CHAR_TO_BIT_MAP['-'])
    assert DNA_CHAR_TO_BIT_MAP['V'] == complement(DNA_CHAR_TO_BIT_MAP['B'])
