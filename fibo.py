from pathlib import Path

# recursive
def fib_recur(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib_recur(num - 2) + fib_recur(num - 1)


# with memoization
cache = {}
def fib_mem(num):

    if num in cache:
        return cache[num]

    if num == 0:
        res = 0
    elif num == 1 or num == 2:
        res = 1
    else:
        res = fib_mem(num - 2) + fib_mem(num - 1)

    cache[num] = res

    return res


def fibo():

    num = int(Path('data/rosalind_fibo.txt').read_text())

    assert fib_recur(num) == fib_mem(num)

    print(fib_mem(num))

fibo()


