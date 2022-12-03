N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
even = set()
odd = set()
for num in numbers:
    if num % 2 == 0:
        if len(even) < 2:
            even.add(num)
    else:
        if len(odd) < 2:
            odd.add(num)
maximum = max(sum(even), sum(odd))
if maximum % 2 == 0:
    print(maximum)
else:
    print(-1)