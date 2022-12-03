# simple sum
# A, B, C = map(int, input().split())
# ans = (A * (A + 1)) // 2 *  (B * (B + 1)) // 2 * (C * (C + 1)) // 2
# print(ans % 998244353)

# # travelling salesman
# K, N = map(int, input().split())
# houses = list(map(int, input().split()))
# distance = list()
# for i in range(N):
#     if i == N-1:
#         distance.append(K - houses[i] + houses[0])
#     else:
#         distance.append(houses[i + 1] - houses[i])
# shortest_dist_travelled = K - max(distance)
# print(shortest_dist_travelled)

# # abc200c
# N = int(input())
# numbers = list(map(int, input().split()))
# from collections import defaultdict
# counter = defaultdict(int)
# for i in range(N):
#     if (numbers[i] % 200) not in counter.keys():
#         counter[numbers[i] % 200] = 1
#     else:
#         counter[numbers[i] % 200] += 1
# pairs = 0
# print(counter)
# for val in counter.values():
#     pairs += (val * (val + 1)) // 2
# print(pairs)

# # hamming distance
# def hamming_distance(dna, pattern):
#     counter = 0
#     if len(dna) != len(pattern):
#         return -1
#     for i in range(len(dna)):
#         if dna[i] != pattern[i]:
#             counter += 1
#     return counter

# print(hamming_distance('AAAAA', 'AAATA'))

# def pattern_count(text, pattern, d):
#     count = 0
#     for i in range(len(text) - len(pattern)):
#         curr = text[i:i+len(pattern)]
#         if hamming_distance(pattern, curr) <= d:
#             count += 1
#     return count

# print(pattern_count('AACAAGCATAAACATTAAAGAG', 'AAAAA', 1))
# # print(pattern_count('AACAAGCATAAACATTAAAGA', 'AAAAA', 1))

# N = int(input())
# S = input()
# counter = 1
# pairs = 0
# for i in range(N-1):
#     print(S[i], S[i+1])
#     if S[i] == S[i+1]:
#         print('..')
#         counter += 1
#     if i == N-2:
#         counter += 1
#         print(counter)
#         pairs += (counter * (counter - 1)) / 2
#         continue
#     else:
#         print('here')
#         pairs += (counter * (counter - 1)) / 2
#         counter = 1
    
# print(pairs)
'''
# billiard
A, B, C, D = map(int, input().split())
neg_B = -B
#equation of a line: y = mx + c
m = (B - D) / (A - C)
c = neg_B - (m * A)
# When y is zero
x = -c / m
print(m, c)
print(x)

# many balls
N = int(input())
inv_str = ''
while N != 0:
    if N % 2 == 0:
        N /= 2
        inv_str += 'B'
    else:
        N -= 1
        inv_str += 'A'
print(inv_str)
ans = ''
for i in range(len(inv_str)-1, -1, -1):
    ans += inv_str[i]
print(ans)
'''
# everyone is friends
N = int(input())
from collections import defaultdict
attendees = defaultdict(set)
for i in range(N):
    print(i)
    party = list(map(int, input().split()))
    print(party)
    for j in range(1, len(party)):
        print(j)
        attendees[party[j]].add(i)
print(attendees)


