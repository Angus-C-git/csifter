import pytest

# CONFIG
from csifter.sifter import sift
fmtstrings_test_file = './modules/fmtstrings.c'  
vulnerable_lines = [
	42, 65,
	43, 68,
	44, 72,
	45, 76,
	46, 80,
	47, 85,
	48, 90,
	49, 95,
	53, 104,
	54, 108,
	57, 114,
	58, 117,
	59, 121,
	60, 125,
]


def test_fmtstrings_found():
	found_blocks = sift(fmtstrings_test_file)
	assert len(found_blocks) == 28


def test_fmtstring_src_ref():
	""" test the lines format string
	vulnerabilities were identified on
	"""
	blocks = sift(fmtstrings_test_file)
	
	for block_no, line in enumerate(vulnerable_lines):
		assert blocks[block_no][1] == line