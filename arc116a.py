import sys
s = [int(line.strip('\n')) for line in sys.stdin.readlines()]
N = s[0]
for i in range(1, N+1):
    if s[i] % 2 == 1:
        print('Odd')
    elif s[i] % 4 == 0:
        print('Even')
    else:
        print('Same')