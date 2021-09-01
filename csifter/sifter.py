from rich import print
from regex import search as regsearch

from csifter.database.db import signatures
from csifter.ui.sifts import render_blocks

'''
‣ Runs primary logic for analysis
'''

def search_pattern(rule, target):
    """ search src file for rule """
    with open(target, 'r') as src:
        return regsearch(rule, src.read()) 


def resolve_block(signature, result, target):
    """ 
    creates a block which encapsulates
    the affected code.

    block:
        signature: the rule that matched
                   the source code block
        line_no: the line where the 
                 identified block 
                 starts
        snippet: the source code which
                 was matched by the rule
    """
    with open(target, 'r') as src:
        line_no = src.read()[:result.start()].count('\n') + 1
        snippet = result.group()
        return (signature, line_no, snippet)


def sift(target):
    """ 
    pass over target file searching for
    source code which matches a rule.

    target: the path to the current
            candidate for source analysis
    """
    blocks_of_intrest = []
    for signature in signatures:
        for rule in signature['rules']:
            result = search_pattern(rule, target)
            if result is not None:
                blocks_of_intrest.append(
                    resolve_block(signature, result, target)
                )
    
    # render blocks
    render_blocks(blocks_of_intrest)
