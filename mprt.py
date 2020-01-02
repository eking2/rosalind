from pathlib import Path
from collections import defaultdict
import requests
import re

class mprt_runner:

    def __init__(self, fn):

        self.matches = defaultdict(list)
        self.uniprots = Path(fn).read_text().splitlines()

    def download_fasta(self, uniprot):

        # download fasta
        url = 'http://www.uniprot.org/uniprot/{}.fasta'.format(uniprot)
        r = requests.get(url)

        # sequence begins from 2nd line
        seq = ''.join(r.text.splitlines()[1:])
        
        return seq

    def find_motif(self, seq):

        # regex to find glycosylation motif
        # find overlapping with lookahead
        matches = re.finditer(r'(?=(N[^P][ST][^P]))', seq)

        # convert start locations to 1 index
        starts = [match.start() + 1 for match in matches]

        return starts

    def run_all(self):

        # run search over all uniprots
        for uniprot in self.uniprots:
            seq = self.download_fasta(uniprot)
            starts = self.find_motif(seq)

            self.matches[uniprot] = starts

        # print results
        for key, value in self.matches.items():
            # only print if matches found
            if len(value) > 0:
                print(key)
                print(' '.join(map(str, value)))


mprt = mprt_runner('data/rosalind_mprt.txt')
mprt.run_all()
