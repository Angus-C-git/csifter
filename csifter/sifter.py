from rich import print
from regex import finditer as regxsearch

from csifter.database.db import signatures
from csifter.ui.report import render_report

'''
‣ Runs primary logic for analysis
'''

def search_pattern(rule, target):
    """ search src file for rule """
    with open(target, 'r') as src:
        return regxsearch(rule, src.read())


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


def sift(target, limit=None, no_warn=False):
    """ 
    pass over target file searching for
    source code which matches a rule
    in the database

    target: the path to the current
            candidate for source analysis
    """
    blocks_of_interest = []
    for signature in signatures:
        if signature['type'] == 'warning' and no_warn:
            break
        for rule in signature['rules']:
            results = search_pattern(rule, target)

            if (
                limit is not None 
                and len(blocks_of_interest) >= limit
            ): break

            for match in results:
                blocks_of_interest.append(
                    resolve_block(
                        signature, 
                        match, 
                        target
                    )
                )

    # render blocks
    render_report(blocks_of_interest)
    return blocks_of_interest
