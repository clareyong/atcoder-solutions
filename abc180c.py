import math
N = int(input())
def prime(number):
    for i in range(2, int(math.sqrt(number))+1):
        if number == 2:
            return True
        if number % i == 0 and i != number:
            return False
    return True
if N == 1:
    print(1)
    exit()
if prime(N):
    print(1)
    print(N)
else:
    num_set
    for i in range(1, N+1):
        if N % i == 0:
            print(i)
