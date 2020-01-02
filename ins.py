from pathlib import Path

def insertion_sort(vals):

    '''
    1. assume first element is sorted
    2. compare value of second element to first
        - if second is larger do nothing
        - if second is smaller then swap position with first
    3. move forward and repeat, check against sorted portion of list
        - insert new element into sorted position
    '''

    swaps = 0

    # start on 2nd element
    for i in range(1, len(vals)):

        # next value to check
        item_to_insert = vals[i]

        # index of prev element
        j = i - 1

        # move all items of sorted segment forward if larger than interted item
        while (j >= 0) and vals[j] > item_to_insert:

            # switch current val (j+1) with last val (j)
            # repeat until sorted up to index j
            vals[j + 1] = vals[j]
            j -= 1

            # count
            swaps += 1

        # insert
        vals[j + 1] = item_to_insert

    return swaps


def ins():

    # insertion sort and count number of swaps required
    n, vals = Path('data/rosalind_ins.txt').read_text().splitlines()
    vals = list(map(int, vals.split()))

    swaps = insertion_sort(vals)

    print(swaps)


ins()

