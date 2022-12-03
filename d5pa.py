N = int(input())
frames = list(map(int, input().split()))
average = sum(frames) / N
if average in frames:
    print(frames.index(average))
    exit()
else:
    difference = 101
    index = 0
    for i in range(N):
        if abs(frames[i] - average) < difference:
            difference = abs(frames[i] - average)
            index = i
    print(index)

