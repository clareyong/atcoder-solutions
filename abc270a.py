A, B = map(int, input().split())

# There are 3 problems, 1, 2 and 4
# if all three are solved, score is 7
# if two are solved, score is 3, 5 or 6
# if one is solved, score is 1, 2 or 4
score_set = set()
def add_score(A, score_set):
    if A == 1 or A == 2 or A == 4:
        score_set.add(A)
    elif A == 3:
        score_set.add(1)
        score_set.add(2) 
    elif A == 5:
        score_set.add(1)
        score_set.add(4) 
    elif A == 6:
        score_set.add(4)
        score_set.add(2) 
    elif A == 7:
        score_set.add(1)
        score_set.add(4)
        score_set.add(2) 
    return score_set
score = add_score(A, score_set)
score = add_score(B, score_set)
print(sum(score))