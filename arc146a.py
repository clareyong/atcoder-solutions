N = int(input())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
new_list = numbers[0:3]
for i in range(3):
    new_list[i] = str(new_list[i]) + 'A'
new_list.sort(reverse=True)
for i in range(3):
    new_list[i] = new_list[i].rstrip('A')
new_number = str(new_list[0]) + str(new_list[1]) + str(new_list[2])
print(new_number)
