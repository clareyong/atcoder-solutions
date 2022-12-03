N, A, B = map(int, input().split())
in_range = list()
for i in range(N+1):
    total = 0
    curr = list(str(i))
    for c in curr:
        total += int(c)
    if total >= A and total <= B:
        in_range.append(int(''.join(curr)))
print(sum(in_range))