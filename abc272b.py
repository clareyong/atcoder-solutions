N, M = map(int, input().split())
p = [set() for i in range(N)]
parties = list()
for i in range(M):
    party = list(map(int, input().split()))
    parties.append(party)
for i, party in enumerate(parties):
    for j in range(1, party[0]+1):
        p[party[j]-1].add(i+1)
counter = 0
for i in range(N):
    for j in range(i+1, N):
        if len(p[i].intersection(p[j])) > 0:
            counter += 1
if counter == N:
    print('Yes')
else:
    print('No')