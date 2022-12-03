n, m = map(int, input().split())
numbers = list(map(int, input().split()))

total = int(-1e18)
for i in range(0, n+1-m):
    temp_total = 0
    for j in range(m):
        temp_total += numbers[i+j] * (j+1)
    if temp_total > total:
        total = temp_total

print(total)
    