N = int(input())
from collections import defaultdict
ladders = defaultdict(list)
for i in range(N):
    ladder = tuple(map(int, input().split()))
    ladders[ladder[0]].append(ladder[1])
    ladders[ladder[1]].append(ladder[0])

def search(root, graph):
    visited = set()
    waitlist = set([root])
    while waitlist:
        cur = waitlist.pop()
        
        if cur in visited:
            continue
        visited.add(cur)

        for neib in graph[cur]:
            if neib in visited:
                continue
            waitlist.add(neib)
    return visited

print(max(search(1, ladders)))