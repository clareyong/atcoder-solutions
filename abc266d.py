number = int(input())
snakes = list()
for i in range(number):
    snake = tuple(map(int, input().split()))
    snakes.append(snake)

curr_pos = 0
time_now = 0
score = 0
steps = 0
for snake in snakes:
    if snake[0] - time_now >= snake[1] - curr_pos:
        print(snake)
        score += snake[2]
        time_now = snake[0]
        curr_pos = snake[1]
    else:
        steps += snake[0] - time_now

print(score)