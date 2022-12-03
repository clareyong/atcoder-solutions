from re import L


n = int(input())
binary = bin(n)
if n == 0:
    print(0)
    exit()
str_bin = str(binary)[2:]
counter = 0
for c in str_bin:
    if c == '1':
        counter + 1
short = '1'*counter
for i in range(n):
    number = bin(i)
    if short not in number:
        print(number)

