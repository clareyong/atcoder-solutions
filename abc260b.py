N, X, Y, Z = map(int, input().split())
maths = list(map(int, input().split()))
eng = list(map(int, input().split()))
students = list()
for i in range(N):
    students.append(((maths[i] + eng[i]), i))
print(students)
students.sort(reverse=True)
print(students)
sorted_math = sorted(maths, reverse=True)
sorted_eng = sorted(eng, reverse=True)
for i in range(X):
    print('math', maths.index(sorted_math[i])+1)
for i in range(Y):
    print('eng', eng.index(sorted_eng[i])+1)
for i in range(Z):
    print('stu', students[i][1]+1)
