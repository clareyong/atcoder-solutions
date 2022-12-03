A, B, C, D = map(int, input().split())
num_list = set()
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for i in range(A, B+1):
    for j in range(C, D+1):
        if is_prime(i+j):
            num_list.add(i)
if len(num_list) == (B-A+1):
    print('Aoki')
else:
    print('Takahashi')
