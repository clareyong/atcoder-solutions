N = int(input())
numbers = list(map(int, input().split()))
X = int(input())
per_set = sum(numbers)
total = (X // per_set) * N
remainder = X % per_set
curr = 0
for i in range(N):
    if (curr + numbers[i]) <= remainder:
        curr += numbers[i]
        total += 1
    else:
        break
print(total+1)
