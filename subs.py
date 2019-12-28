from pathlib import Path
import re

def subs():

    template, substring = Path('data/rosalind_subs.txt').read_text().strip().splitlines()

    # use lookahead to get overlapping matches
    matches = re.finditer('(?={})'.format(substring), template)
    match_idxs = list(x.start()+1 for x in matches)
    print(' '.join(map(str, match_idxs)))

subs()
