N = int(input())
first = ['H', 'D', 'C', 'S']
second = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
words = set()
for i in range(N):
    s = input()
    if s[0] in first and s[1] in second and not s in words:
        words.add(s)
    else:
        print('No')
        exit()
print('Yes')
