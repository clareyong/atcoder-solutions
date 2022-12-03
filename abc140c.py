N = int(input())
numbers = list(map(int, input().split()))
numbers = [1e6] + numbers + [1e6]
# print(numbers)
total = 0
for i in range(N):
    total += min(numbers[i], numbers[i+1])
print(total)