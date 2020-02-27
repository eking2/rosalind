from pathlib import Path

def parse_input():

    n, k = Path('data/rosalind_fib.txt').read_text().split()

    return int(n), int(k)

# store prev answers
memo = {}
def fib(n, k):
    
    '''
    F_n = number of rabbits in the nth generation
    F_1 = F_2 = 1

    F_n = F_{n-1} + k * F_{n-2}
    '''
    args = (n, k)

    if (n, k) in memo:
        return memo[args]

    # base case
    if n <= 2:
        result = 1
    else:
        result = fib(n - 1, k) + k * fib(n-2, k)

    memo[args] = result

    return result

n, k = parse_input()
result = fib(n, k)
print(result)
  
    

