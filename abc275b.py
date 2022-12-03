A, B, C, D, E, F = map(int, input().split())
A %= 998244353
B %= 998244353
C %= 998244353
D %= 998244353
E %= 998244353
F %= 998244353

abc_ = A * B * C
def_ = D * E * F
difference = abc_ - def_
print(difference % 998244353)