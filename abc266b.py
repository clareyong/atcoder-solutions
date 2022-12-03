N = int(input())
number = 998244353
modulo = N % number

print(modulo) 

# lower = N // number
# upper = lower + 1

# new_number_upper = int(number * upper) 
# new_number_lower = int(number * lower)

# difference_upper = int(N - new_number_upper)
# difference_lower = int(N - new_number_lower)

# if difference_lower >= 0:
#     print(difference_lower)
# else:
#     print(difference_upper)