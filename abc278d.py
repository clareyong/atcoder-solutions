import sys
from collections import defaultdict
s = [item.strip() for item in sys.stdin.readlines()]
N = int(s[0])
numbers = list(map(int, s[1].split()))
Q = int(s[2])
offset = defaultdict(int)
reset = -1
reseted = False
for i in range(3, Q+3):
    curr = tuple(map(int, s[i].split()))
    if curr[0] == 1:
        reset = curr[1]
        reseted = True
        offset = defaultdict(int)
    elif curr[0] == 2 and reseted == False:
        numbers[curr[1]-1] += curr[2]
    elif curr[0] == 2 and reseted == True:
        offset[curr[1]-1] += curr[2]
    elif curr[0] == 3 and reseted == False:
        print(numbers[curr[1]-1])
    elif curr[0] == 3 and reseted == True:
        print(reset + offset[curr[1]-1])

