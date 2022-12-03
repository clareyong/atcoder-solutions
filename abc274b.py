H, W = map(int, input().split())
lines = list()
for i in range(H):
    lines.append(input())
count = [0] * W
for i in range(H):
    for j in range(W):
        if lines[i][j] == '#':
            count[j] += 1
answer = ' '.join(str(c) for c in count)
answer = answer.strip()
print(answer)