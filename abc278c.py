import sys
s = [item.strip() for item in sys.stdin.readlines()]
from collections import defaultdict
counter = defaultdict(set)
N, Q = map(int, s[0].split())
for i in range(1, Q+1):
    curr = tuple(map(int, s[i].split()))
    if curr[0] == 1:
        counter[curr[1]].add(curr[2])
    elif curr[0] == 2:
        if curr[2] in counter[curr[1]]:
            counter[curr[1]].remove(curr[2])
    else:
        if curr[1] in counter[curr[2]] and curr[2] in counter[curr[1]]:
            print('Yes')
        else:
            print('No')
