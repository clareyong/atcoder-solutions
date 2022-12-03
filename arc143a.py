A, B, C = sorted(map(int, input().split()))
na = A + B - C
nb = C - A
nc = C - B
if na < 0:
    print(-1)
    exit()
print(na+nb+nc)
