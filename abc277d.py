N, M = map(int, input().split())
cards = list(map(int, input().split()))
sum_of_cards = sum(cards)
cards.sort()
total = list()
group = cards[0]
for i in range(1, N):
    if cards[i] - cards[i-1] > 1:
        total.append(group)
        group = cards[i]
    else:
        group += cards[i]
if group == sum_of_cards:
    print(0)
    exit()
total.append(group)
if len(total) == 1:
    print(0)
elif cards[-1] + 1 == M and cards[0] == 0:
    total.append(total[0] + total[-1])
    print(sum_of_cards - max(total))
else:
    print(sum_of_cards - (max(total)))

