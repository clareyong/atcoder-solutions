import sys
s = [int(line.strip('\n')) for line in sys.stdin.readlines()]
N = s[0]
for i in range(1, N+1):
    # print(i)
    curr = s[1:i] + s[i+1:]
    # print(curr)
    print(max(curr))
