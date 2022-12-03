N = int(input())
string = input()
if string[0] != string[-1]:
    print(1)
    exit()
else:
    for i in range(1, N):
        if string[i] != string[0] and string[i+1] != string[0]:
            print(2)
            exit()
print(-1)
