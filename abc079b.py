N = int(input())
numbers = [2, 1]
for i in range(2, N+1):
    numbers.append(numbers[i-1] + numbers[i-2])
print(numbers[-1])