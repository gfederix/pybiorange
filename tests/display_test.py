import numpy as np
import pytest

from bioranges import show_table
from bioranges.show_table import RowComposer
from bioranges.show_table import RowPresenter
# local


def test_epty_show_table():
    assert show_table() == ''


@pytest.mark.skip()
def test_single_column_show_table():
    out_str = show_table([('first_name', [1, 2, 3])])
    assert out_str == (
        'first_name\n'
        '    <list>\n'
        '         1\n'
        '         2\n'
        '         3')


@pytest.mark.skip()
def test_single_column_show_table_if_name_smaller_than_type_name_must_detect_size_by_len_type_name():
    out_str = show_table([('x', [1, 2, 3])])
    assert out_str == (
        '     x\n'
        '<list>\n'
        '     1\n'
        '     2\n'
        '     3')


def test_row_presenter_align_by_name():
    assert list(RowPresenter('my_name', 't', [1, 2, 3], 5)) == [
        'my_name',
        '    <t>',
        '      1',
        '      2',
        '      3']


def test_row_presenter_align_by_type_name():
    assert list(RowPresenter('name', 'my_type', [1, 2, 3], 5)) == [
        '     name',
        '<my_type>',
        '        1',
        '        2',
        '        3']


def test_row_presenter_align_by_number():
    assert list(RowPresenter('name', 't', [1000000, 2, 3], 5)) == [
        '   name',
        '    <t>',
        '1000000',
        '      2',
        '      3']


def test_row_presenter_align_by_min_row_width():
    assert list(RowPresenter('name', 't', [1, 2, 3], 5)) == [
        ' name',
        '  <t>',
        '    1',
        '    2',
        '    3']


def test_row_compouser():
    assert list(RowComposer(
        RowPresenter('name1', 'my_type', [1, 2, 3], 5),
        RowPresenter('name2', 'my_type', [1, 2, 3], 5)
    )) == [
        '    name1     name2',
        '<my_type> <my_type>',
        '        1         1',
        '        2         2',
        '        3         3']
