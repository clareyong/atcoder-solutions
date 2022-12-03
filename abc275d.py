N = int(input())
results = dict()
def recursion(n):
    if n == 0:
        return 1
    else:
        if n in results:
            return results[n]
        else:
            results[n] = recursion(n//2) + recursion(n//3)
            return results[n]
print(recursion(N))