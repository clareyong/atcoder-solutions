from typing import Mapping


N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_a = a[0]
ans = a[0] * b[0]
print(ans)
for i in range(1, N):
    max_a = max(max_a, a[i])
    curr = max_a * b[i]
    if curr > ans:
        ans = curr
    print(ans)