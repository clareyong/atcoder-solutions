N, D, H = map(int, input().split())
locations = list()
for i in range(N):
    d, h = map(int, input().split())
    locations.append((d, h))
# y = mx + c
y_intercept = list()
for location in locations:
    m = (H-location[1]) / (D-location[0])
    c = H - m * D
    y_intercept.append(c)
if max(y_intercept) >= 0:
    print(max(y_intercept))
else:
    print(0.0)