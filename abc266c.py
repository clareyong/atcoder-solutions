sides = list()
for i in range(4):
    sides.append(list(map(int, input().split())))
set_1 = sides[0:3]
set_2 = sides[1:4]
set_3 = sides[2:4]
set_3.append(sides[0])
set_4 = sides[0:2]
set_4.append(sides[3])
def calc_cross(set):
    dx1 = set[0][0] - set[1][0]
    dx2 = set[1][0] - set[2][0]
    dy1 = set[0][1] - set[1][1]
    dy2 = set[1][1] - set[2][1]
    return (dx1 * dy2 - dx2 * dy1)

cross_1 = calc_cross(set_1)
cross_2 = calc_cross(set_2)
cross_3 = calc_cross(set_3)
cross_4 = calc_cross(set_4)

if cross_1 > 0 and cross_2 > 0 and cross_3 > 0 and cross_4 > 0:
    print('Yes')
elif cross_1 < 0 and cross_2 < 0 and cross_3 < 0 and cross_4 < 0:
    print('Yes')
else:
    print('No')