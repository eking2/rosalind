from pathlib import Path
from Bio import Entrez

def gbk():

    genus, date1, date2 = Path('data/rosalind_gbk.txt').read_text().splitlines()

    Entrez.email = 'edwking@live.com'

    # get number of records for target organism between dates
    search_term = f'"{genus}"[Organism] AND ("{date1}"[PDAT] : "{date2}"[PDAT])' 
    handle = Entrez.esearch(db='nucleotide', term=search_term)
    record = Entrez.read(handle)

    print(record['Count'])
    
gbk()
