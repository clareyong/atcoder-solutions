import sys
s = [line.strip('\n') for line in sys.stdin.readlines()]
N, K = int(s[0]), int(s[1])
balls = list(map(int, s[2].split()))
total = 0
for ball in balls:
    total += min(2*ball, 2*(K-ball))
print(total)