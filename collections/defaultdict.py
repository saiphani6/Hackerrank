"""
Problem link: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
"""

from collections import defaultdict

m, n = input().split()
m, n = int(m), int(n)
m_default_dict = defaultdict(list)
for i in range(1, m+1):
    m_default_dict[input()].append(str(i))

required_input = []
for j in range(1, n+1):
    required_input.append(input())

for input_ in required_input:
    print(' '.join(m_default_dict.get(input_, str(-1))))