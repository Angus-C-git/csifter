from rich import print
# import re

from regex import search as regsearch

from csifter.database.signatures import signatures
from csifter.ui.sifts import render_blocks


'''
‣ Runs primary logic for analysis
'''


def sift(target):
    """ pass over target file """
    
    blocks_of_intrest = []

    # walk rules and compare to current line
    with open(target, 'r', encoding='utf-8') as src:
        for line in src:
            for signature in signatures:
                for rule in signature['rules']:
                    if regsearch(rule, line) is not None:
                        blocks_of_intrest.append(
                            (
                                signature,
                                line
                            )
                        )
    
    # render blocks
    render_blocks(blocks_of_intrest)