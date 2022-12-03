status = input()
one = True
arr = [True, True, True, True, True, True,True]
if status[0] == '0':
    one = False
if status[1] == '0' and status[7] == '0':
    arr[2] = False
if status[3] == '0':
    arr[1] = False
if status[6] == '0':
    arr[0] = False
if status[2] == '0' and status[8] == '0':
    arr[4] = False
if status[4] == '0':
    arr[3] = False
if status[5] == '0':
    arr[5] = False
if status[9] == '0':
    arr[6] = False

state = 0

for i in range(len(arr)):
    if state == 0 and arr[i] == True:
        state += 1
    elif state == 1 and arr[i] == False:
        state += 1
    elif state == 2 and arr[i] == True:
        state += 1
if state == 3 and one == False:
    print('Yes')
else:
    print('No')