s = input()
flag_c = False
flag_f = False
for c in s:
    if c == 'C' and flag_f == False:
        flag_c = True
    elif c == 'F' and flag_c == True:
        flag_f = True
if flag_c == True and flag_f == True:
    print('Yes')
else:
    print('No')