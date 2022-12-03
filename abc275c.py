import math 
lines = list()
for i in range(9):
    lines.append(input())
coordinates = list()
for i in range(9):
    for j in range(9):
        if lines[i][j] == '#':
            coordinates.append((i, j))
length = len(coordinates)
coordinates_set = set(coordinates)
squares = set()
for i in range(length):
    for j in range(i+1, length):
        dx = coordinates[i][0] - coordinates[j][0]
        dy = coordinates[i][1] - coordinates[j][1]
        p1 = (coordinates[i][0] + dy, coordinates[i][1] - dx) 
        p2 = (coordinates[j][0] + dy, coordinates[j][1] - dx) 
        p3 = (coordinates[i][0] - dy, coordinates[i][1] + dx) 
        p4 = (coordinates[j][0] - dy, coordinates[j][1] + dx) 
        if p1 in coordinates_set and p2 in coordinates_set:
            squares.add(tuple(sorted((p1, p2, coordinates[i], coordinates[j]))))
        if p3 in coordinates_set and p4 in coordinates_set:
            squares.add(tuple(sorted((p3, p4, coordinates[i], coordinates[j]))))
print(len(squares))