import pytest
from bioranges import show_table
import numpy as np

def test_sum():
    assert 1 + 1 == 2

def test_epty_show_table():
    assert show_table() == ""

def test_single_column_show_table():
    out_str = show_table([("first_name", [1, 2, 3])])
    assert out_str == "first_name\n<list>\n1\n2\n3"
