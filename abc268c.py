# number = int(input())
# dishes = list(map(int, input().split()))
# maximum = 0
# for i in range(0, number):
#     dish_list = list()
#     counter = 0
#     for j in range(number):
#         offseted_j = j-i
#         if j == dishes[offseted_j] or j == dishes[(offseted_j-1) % number] or j == dishes[(offseted_j+1) % number]:
#             counter += 1
#     if counter > maximum:
#         maximum = counter
# print(maximum)



number = int(input())
dishes = list(map(int, input().split()))
buckets = [0] * number
for i in range(0, number):
    offset = (dishes[i] - i) % number
    # print(f"ey dish {dishes[i]} is wrong placed by {offset} places")
    buckets[offset] += 1
# print(buckets)
max_v = 0
for i in range(0, number):
    total = buckets[i] + buckets[(i+1) % number] + buckets[(i+2) % number]
    max_v = max(max_v, total)
print(max_v)