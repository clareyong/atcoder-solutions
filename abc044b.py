from collections import defaultdict
s = input()
counter = defaultdict(int)
for c in s:
    counter[c] += 1
for val in counter.values():
    if val % 2 == 1:
        print('No')
        exit()
print('Yes')