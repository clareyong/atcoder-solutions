N, M = map(int, input().split())
arr = [[] for x in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    arr[A-1].append(B)
    arr[B-1].append(A)
for item in arr:
    if len(item) == 0:
        print(0)
    else:
        item.sort()
        ans = ' '.join(str(i) for i in item)
        ans.strip()
        print(len(item), ans)