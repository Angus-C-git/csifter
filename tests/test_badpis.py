import pytest

from csifter.sifter import sift
badapis_src_file = './modules/badapis.c'
vulnerable_lines = [
    46, 60,
    47, 66,
    48, 71,
    49, 77,
    51,
    52, 82,
    54, 86,
    55, 89
]


def test_detection():
    assert len(sift(badapis_src_file)) == 15


def test_src_refs():
    blocks = sift(badapis_src_file)
    for block_no, line in enumerate(vulnerable_lines):
        assert blocks[block_no][1] == line