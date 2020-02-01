from collections import Counter
from pathlib import Path

def maj():

    arr = Path('data/rosalind_maj.txt').read_text().splitlines()

    # k arrays
    # each array is size n
    k, n = map(int, arr[0].split())

    result = []
    for line in arr[1:]:

        count_nums= Counter(line.split())

        # tuple of (value, count)
        # index 0 is most common value
        most_common = count_nums.most_common()[0]

        count = most_common[1]
        # check if most common value occurs more than n/2 times
        if count > n/2:
            result.append(most_common[0])
        else:
            result.append(-1)

    # print result
    print(' '.join(map(str, result)))

maj()
