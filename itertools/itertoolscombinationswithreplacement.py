"""
Problem link:
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""

import itertools

S, K = input().split()

print('\n'.join(sorted([''.join(sorted(combination)) for combination in itertools.combinations_with_replacement(S, int(K))])))
