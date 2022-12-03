a, b = map(int, input().split())
difference = b - a
def summation(number):
    if number == 1:
        return 1
    else:
        return number + summation(number-1)
print(summation(difference)-b)