import math
N = int(input())
amoeba = list(map(int, input().split()))
gen = [0]
for am in amoeba:
    gen.append(gen[am-1]+1)
    gen.append(gen[am-1]+1)
answer = '\n'.join(str(c) for c in gen)
answer = answer.strip()
print(answer)