from pathlib import Path
import itertools

def lexv():

    letters, num = Path('data/rosalind_lexv.txt').read_text().strip().splitlines()
    num = int(num)

    # add blank char
    letters = [' '] + letters.split()

    # make all combinations 
    combos = []
    for i in range(1, num + 1):
        combos.extend([''.join(x) for x in itertools.product(letters, repeat=i)])

    # remove space char
    # drop duplicates and empty
    combos = list(set([x.replace(' ', '') for x in combos]))
    combos.remove('')

    # sort by order of input letters
    combos.sort(key = lambda word: [letters.index(x) for x in word])

    for combo in combos:
        print(combo)

    # print
    #with open('text.txt', 'w') as fo:
    #    for combo in combos:
    #        fo.write('{}\n'.format(combo))

lexv()


