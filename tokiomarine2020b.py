A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
difference = abs(B - A)
a_travel = V * T
b_travel = W * T
if a_travel >= b_travel + difference:
    print('YES')
else:
    print('NO')
