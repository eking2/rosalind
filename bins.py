from pathlib import Path


def binary_search(to_search, val):

    '''
    1. input sorted array and value to search for
    2. check middle element in array 
        - if match then return the middle index
    3. if no match then compare middle element to target value to determine 
       which side to check next
       - get first occurence by going backward on match
    4. repeat until match or no more elements to check
    '''

    # start and end idx
    first = 0
    last = len(to_search) - 1

    while (first <= last):

        # get index of middle element
        mid = (first + last) // 2

        # val greater than mid, go right
        if to_search[mid] < val:
            first = mid + 1

        # val less than mid, go left
        elif to_search[mid] > val:
            last = mid - 1

        # get first occurence
        # on match set end to current and check from first
        elif first != mid:
            last = mid

        # 1-index solution
        else:
            return mid + 1

    # no match
    return -1


def bins():

    # perform binary search
    # find index for all vals in to_search
    # return -1 if not found
    n, m, to_search, vals = Path('data/rosalind_bins.txt').read_text().splitlines()
    to_search = list(map(int, to_search.split()))
    vals = list(map(int, vals.split()))

    assert int(n) == len(to_search)
    assert int(m) == len(vals)

    results = [binary_search(to_search, val) for val in vals]

    print(' '.join(map(str, results)))
    #Path('bins_out.txt').write_text(' '.join(map(str, results)))

bins()
