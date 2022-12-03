from re import L


H, W = map(int, input().split())
grid = list()
for i in range(H):
    grid.append(list(input().split()))
for i in range(H):
    if 'snuke' in grid[i]:
        target = i
        break
for i in range(W):
    if grid[target][i] == 'snuke':
        horizontal = chr(i + 65)
        vertical = str(target+1)
        print(horizontal+vertical)
