from collections import defaultdict
H, W = map(int, input().split())
counter_s = [[] for _ in range(W)]
counter_t = [[] for _ in range(W)]
s = list()
t = list()
for i in range(H):
    s.append(input())
for i in range(H):
    t.append(input())
for item in s:
    for i, c in enumerate(item):
        counter_s[i] += c
for item in t:
    for i, c in enumerate(item):
        counter_t[i] += c
counter_s.sort()
counter_t.sort()
if counter_s == counter_t:
    print('Yes')
else:
    print('No')