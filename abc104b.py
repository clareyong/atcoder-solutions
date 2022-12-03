s = input()
flag = False
section = s[2:len(s)-1]
if s[0] != 'A':
    print('WA')
    exit()
if s[1].isupper():
    print('WA')
    exit()
if s[-1] == 'C' or s[-1].isupper():
    print('WA')
    exit()
for c in section:
    if c == 'C':
        if flag == True:
            print('WA')
            exit()
        else:
            flag = True
    elif c.isupper() and c != 'C':
        print('WA')
        exit()
if flag == True:
    print('AC')
else:
    print('WA')