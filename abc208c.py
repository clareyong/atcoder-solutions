import sys
s = sys.stdin.readlines()
N, K = map(int, s[0].split())
id = list(map(int, s[1].split()))
length = len(id)
remaining = K % length
# candies = [K//length] * length
id_min = set(sorted(id)[0:remaining])
for i in range(length):
    if id[i] in id_min:
        print(K//length + 1)
    else:
        print(K//length)