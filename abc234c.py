N = int(input())
num_list = list()
def DecimalToBinary(num, num_list):
    if num >= 1:
        DecimalToBinary(num // 2, num_list)
        num_list.append(num % 2)
    return num_list

new_list = DecimalToBinary(N, num_list)
for i in range(len(new_list)):
    if new_list[i] == 1:
        new_list[i] = 2
answer = ''
for number in new_list:
    number = str(number)
    answer += number
print(answer)