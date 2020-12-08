import pytest

from bioranges.struct import complement
from bioranges.struct import DNA_CHAR_TO_BIT_MAP
from bioranges.struct import DNAStr
from bioranges.struct import DNAVec


def test_dna_string():
    dna = DNAStr('ATGC')
    assert len(dna) == 4


def test_dna_string_compare():
    assert DNAStr('ATGC') == DNAStr('ATGC')


def test_dna_string_repr():
    assert DNAStr('ATGC').__repr__() == 'ATGC'


def test_binarization():
    DNAStr.tobit('A') == 0b1


def test_complement():
    x = DNAStr('AGTC')
    assert x.complement() == DNAStr('TCAG')


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
    d0 = DNAVec()
    assert list(d0) == []
    d1 = DNAVec(['ATC', 'GCA'])
    assert list(d1) == [DNAStr('ATC'), DNAStr('GCA')]


def test_dna_vec_resize():
    d1 = DNAVec(['ATC', 'GCA'])
    assert list(d1.resize(2)) == [DNAStr('AT'), DNAStr('GC')]
    assert list(d1.resize(3)) == [DNAStr('ATC'), DNAStr('GCA')]
    assert list(d1.resize(4)) == [None, None]
    assert list(DNAVec(['ATC', 'GCACC']).resize(4)) == [None, DNAStr('GCAC')]
