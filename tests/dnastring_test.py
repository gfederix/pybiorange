import pytest

from bioranges.struct import DNA_BIT_MAP
from bioranges.struct import DNAString


def test_dna_string():
    dna = DNAString('ATGC')
    assert len(dna) == 4


@pytest.mark.skip('TODO')
def test_dna_string_compare():
    assert DNAString('ATGC') == DNAString('ATGC')


def test_binarization():
    DNAString.tobit('A') == 0b1


def test_complementaryity_in_binarization():
    # DNAString.tobit("A") == 0b1
    # DNAString.tobit("T") == 0b1
    assert DNA_BIT_MAP['A'] == ~DNA_BIT_MAP['T']
    assert DNA_BIT_MAP['G'] == ~DNA_BIT_MAP['C']
    assert DNA_BIT_MAP['A'] != DNA_BIT_MAP['G']
