N, K = map(int, input().split())
numbers = list(map(int, input().split()))
if K == 0:
    print(' '.join(str(i) for i in numbers))
    exit()
elif K < N:
    new_list = numbers[K:]
    for i in range(K):
        new_list.append(0)
else:
    new_list = [0] * N
print(' '.join(str(i) for i in new_list))
