N, M = map(int, input().split())
from collections import defaultdict
counter = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    counter[a-1] += 1
    counter[b-1] += 1
roads = list()
for i in range(N):
    print(counter[i])
