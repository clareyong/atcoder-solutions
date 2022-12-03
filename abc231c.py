N, Q = map(int, input().split())
heights = list(map(int, input().split()))
def binarySearch(arr, x, low, high):
    while low != high:
        mid = (low + high)//2
        if (x == arr[mid]):
            return mid
        elif (x > arr[mid]): #x is on the right side
            low = mid + 1
        else: # x is on the left side
            high = mid - 1
print(binarySearch(heights, 2, 0, N))
for i in range(Q):
    x = int(input())

