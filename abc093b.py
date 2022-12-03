A, B, K = map(int, input().split())
numbers = set()
if K > (B - A + 1):
    for i in range(A, B+1):
        print(i)
    exit()
for i in range(K):
    if A <= B:
        numbers.add(A)
        A += 1
    if B >= A:
        numbers.add(B)
        B -= 1
sorted_num = list(numbers)
sorted_num.sort()
for num in sorted_num:
    print(num)