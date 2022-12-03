s = input()
a = -1
z = -1
for i in range(len(s)):
    if s[i] == 'A':
        a = i 
        break
for i in range(len(s)-1, -1, -1):
    if s[i] == 'Z':
        z = i
        break
new_str = s[a:z+1]
print(len(new_str))
