N = int(input())
numbers = list(map(int, input().split()))
curr = -1
max_num = -1
for i in range(0, N-1):
    if numbers[i] > numbers[i + 1]:
        max_num = numbers[i]
        break
if max_num == -1:
    max_num = max(numbers)
for num in numbers:
    if num != max_num:
        print(num, end=' ')
print()