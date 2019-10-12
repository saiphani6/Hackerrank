"""
Problem Statement:

You are given a string S.
Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value K separated by a space.

Constraints
0<K<=len(S)

The string contains only UPPERCASE characters.

Output Format

Print the different combinations of string S on separate lines

Input:

HACK 2

Output:

A
C
H
K
AC
AH
AK
CH
CK
HK
"""

import itertools

S, N = input().split()

all_combinations = []

for i in range(1, int(N)+1):
    all_combinations.extend(sorted([''.join(sorted(combination)) for combination in list(itertools.combinations(S, i))]))

print('\n'.join(all_combinations))
