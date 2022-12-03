import sys
s = [tuple(map(int, line.split())) for line in sys.stdin.readlines()]
# print(s)
N, W = s[0][0], s[0][1]
# cheese = sorted(s[1:], key=lambda x: x[1], reverse=True)
# print(cheese)
cheese = s[1:]
cheese.sort(reverse=True)
tasty = 0
for i in range(N):
    if W - cheese[i][1] >= 0:
        W -= cheese[i][1]
        tasty += cheese[i][0] * cheese[i][1]
    else:
        tasty += cheese[i][0] * W
        break
print(tasty)
