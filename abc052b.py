N = int(input())
S = input()
maximum = 0
count = 0
for c in S:
    if c == 'I':
        count += 1
    else:
        count -= 1
    if count > maximum:
        maximum = count
print(maximum)