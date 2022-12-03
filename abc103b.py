s = input()
t = input()
if s == t:
    print('Yes')
    exit()
for i in range(1, len(s)):
    word = s[i:i+len(s)] + s[0:i]
    if word == t:
        print('Yes')
        exit()
print('No')