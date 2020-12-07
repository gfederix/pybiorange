import pytest

from bioranges.struct import complement
from bioranges.struct import DNA_CHAR_TO_BIT_MAP
from bioranges.struct import DNAString
from bioranges.struct import DNAVec


def test_dna_string():
    dna = DNAString('ATGC')
    assert len(dna) == 4


def test_dna_string_compare():
    assert DNAString('ATGC') == DNAString('ATGC')


def test_dna_string_repr():
    assert DNAString('ATGC').__repr__() == 'ATGC'


def test_binarization():
    DNAString.tobit('A') == 0b1


def test_complement():
    x = DNAString('AGTC')
    assert x.complement() == DNAString('TCAG')


def test_complementaryity_in_binarization():
    def nt(x):
        return DNA_CHAR_TO_BIT_MAP[x]

    def assert_self_complementary_nt(x):
        assert nt(x) == nt(x)

    def assert_complementary_nt(x, y):
        assert nt(x) == complement(nt(y))

    def assert_notcomplementary_nt(x, y):
        assert nt(x) != complement(nt(y))

    assert_notcomplementary_nt('A', 'G')
    assert_notcomplementary_nt('T', 'C')
    assert_notcomplementary_nt('A', 'B')
    assert_complementary_nt('A', 'T')
    assert_complementary_nt('G', 'C')
    assert_complementary_nt('M', 'K')
    assert_complementary_nt('K', 'M')
    assert_complementary_nt('V', 'B')
    assert_self_complementary_nt('W')
    assert_self_complementary_nt('S')
    assert_self_complementary_nt('N')
    assert_self_complementary_nt('-')


def test_dna_vec():
    DNAVec()
