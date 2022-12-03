import sys
from collections import defaultdict
s = [line.strip('\n') for line in sys.stdin.readlines()]
N, K, Q = map(int, s[0].split())
counter = defaultdict(int)
for i in range(Q):
    curr = int(s[i+1])
    counter[curr] += 1
scores = [K] * N
for i in range(N):
    if i+1 not in counter:
        scores[i] -= Q
    else:
        scores[i] -= Q - counter[i+1]
    if scores[i] > 0:
        print('Yes')
    else:
        print('No')