import pytest
import numpy as np

# local
from bioranges import show_table
from bioranges.show_table import row_presenter, cell_presenter, type_cell_presenter


def test_sum():
    assert 1 + 1 == 2


def test_epty_show_table():
    assert show_table() == ""


def test_single_column_show_table():
    out_str = show_table([("first_name", [1, 2, 3])])
    assert out_str == (
        "first_name\n"
        "    <list>\n"
        "         1\n"
        "         2\n"
        "         3")


def test_row_presenter():
    out_array = row_presenter(name="first_name", type="array", data=[1, 2, 3], width=12)
    assert out_array == [
        "  first_name",
        "     <array>",
        "           1",
        "           2",
        "           3"]


def test_cell_presenter():
    assert cell_presenter(100, 5) == "  100"


def test_cell_presenter():
    assert type_cell_presenter("some_type", 15) == "    <some_type>"
