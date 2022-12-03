N = int(input())
P = list(map(int, input().split()))
for i in range(N):
    if P[i] < P[i+1]:
        curr = P[i+2:]
        not_curr = P[:i+2]
        break
print(curr)
print(not_curr)
first_half = ' '.join(str(c) for c in not_curr)
if len(curr) != 0:
    first = curr[0]
curr.sort(reverse=True)
idx = curr.index(first)
starting = curr[idx+1]
# print(curr)
# print(starting)
curr.remove(starting)
second_half = str(starting) + ' ' + ' '.join(str(c) for c in curr)
print(first_half + ' ' + second_half)