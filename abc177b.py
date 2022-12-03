s = input()
t = input()
count = set()
for i in range(len(s)-len(t)+1):
    counter = 0
    for j in range(len(t)):
        curr = s[i:i+len(t)]
        if curr[j] == t[j]:
            counter += 1
    count.add(counter)
print(len(t) - max(count))