import pytest

# CONFIG
from csifter.sifter import sift
fmtstrings_test_file = './modules/fmtstrings.c'  

def test_fmtstrings():
	blocks = sift(fmtstrings_test_file)
	assert blocks[0][1] == 42 

