lines = list()
for i in range(10):
    lines.append(input())
A, B, C, D = -1, -1, -1, -1
for i in range(10):
    for j in range(10):
        if lines[i][j] == '#':
            A = i
            C = j
            break
    if A != -1 and C != -1:
        break
for i in range(C, 10):
    if lines[A][i] == '#':
        D = i
for i in range(A, 10):
    if lines[i][D] == '#':
        B = i
print(A+1, B+1)
print(C+1, D+1)
