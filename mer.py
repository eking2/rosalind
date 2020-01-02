from pathlib import Path


def mer():

    # merge 2 sorted lists
    n, left_list, m, right_list = Path('data/rosalind_mer.txt').read_text().splitlines()
    n, m = int(n), int(m)

    left_list = list(map(int, left_list.split()))
    right_list = list(map(int, right_list.split()))

    assert n == len(left_list)
    assert m == len(right_list)

    sorted_list = []

    # compare values from each list
    # since already sorted we check the 0 index of each
    # will end when one array is empty
    while left_list and right_list:

        # check for smallest value and save
        if left_list[0] < right_list[0]:
            sorted_list.append(left_list.pop(0))
        else:
            sorted_list.append(right_list.pop(0))

    # get remaining number 
    sorted_list.extend(left_list + right_list)

    print(' '.join(map(str, sorted_list)))

mer()
