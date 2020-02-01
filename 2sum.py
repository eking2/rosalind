from pathlib import Path

def sum2():
    
    arr = Path('data/rosalind_2sum.txt').read_text().splitlines()

    # k number of arrays
    # n length each array
    k, n = map(int, arr[0].split())

    result = []
    for line in arr[1:]:

        # loop over each value 
        vals = list(map(int, line.split()))

        # if there are multiple matches in each line
        # save here and sort
        matches = []
        for i, num in enumerate(vals):

            rev = num * -1

            # 0 condition
            if num == 0 and vals.count(0) >= 2:

                # get index of first 2 occurences
                # 1-index
                zero_index = [i for i, x in enumerate(vals) if x == 0]
                p = zero_index[0] + 1
                q = zero_index[1] + 1
                matches.append([p, q])

            # check if reverse sign present
            if rev in vals and num != 0:

                # append to matches
                # 1-index
                # then sort and select lowest q
                p = min(vals.index(rev) + 1, vals.index(num) + 1)
                q = max(vals.index(rev) + 1, vals.index(num) + 1)
                matches.append([p, q])

            # end of loop, no matches
            if i == len(vals) - 1:
                if len(matches) == 0:
                    result.append(-1)
                else:
                    # sort by q then p
                    lowest_q = sorted(matches, key=lambda x: (x[1], x[0]))
                    result.append(lowest_q[0])

    
    for indices in result:
        if isinstance(indices, list):
            print(' '.join(map(str, indices)))
        else:
            print(indices)


sum2()
