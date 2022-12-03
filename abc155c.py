N = int(input())
from collections import defaultdict
counter = defaultdict(int)
for i in range(N):
    s = input()
    counter[s] += 1
maximum = max(counter.values())
max_words = list()
for key, value in counter.items():
    if value == maximum:
        max_words.append(key)
max_words.sort()
for word in max_words:
    print(word)
