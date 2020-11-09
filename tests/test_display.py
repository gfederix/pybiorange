import pytest
import numpy as np

# local
from bioranges import show_table
from bioranges.show_table import row_presenter, cell_presenter, type_cell_presenter, RowPresenter


def test_sum():
    assert 1 + 1 == 2


def test_epty_show_table():
    assert show_table() == ""


@pytest.mark.skip()
def test_single_column_show_table():
    out_str = show_table([("first_name", [1, 2, 3])])
    assert out_str == (
        "first_name\n"
        "    <list>\n"
        "         1\n"
        "         2\n"
        "         3")


@pytest.mark.skip()
def test_single_column_show_table_if_name_smaller_than_type_name_must_detect_size_by_len_type_name():
    out_str = show_table([("x", [1, 2, 3])])
    assert out_str == (
        "     x\n"
        "<list>\n"
        "     1\n"
        "     2\n"
        "     3")

def test_row_presenter_align_by_name():
    assert list(RowPresenter("my_name", "t", [1, 2, 3], 5)) == [
        "my_name",
        "    <t>",
        "      1",
        "      2",
        "      3"]

def test_row_presenter_align_by_type_name():
    assert list(RowPresenter("name", "my_type", [1, 2, 3], 5)) == [
        "     name",
        "<my_type>",
        "        1",
        "        2",
        "        3"]
def test_row_presenter_align_by_number():
    assert list(RowPresenter("name", "t", [1000000, 2, 3], 5)) == [
        "   name",
        "    <t>",
        "1000000",
        "      2",
        "      3"]

def test_row_presenter():
    out_array = row_presenter(name="first_name", type="array", data=[1, 2, 3], min_width=12)
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
