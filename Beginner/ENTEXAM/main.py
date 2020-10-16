t = int(input())
for _ in range(t):
    n, k, e, m = map(int, input().split())
    students = []
    for _ in range(n-1):
        score = sum(list(map(int, input().split())))
        students.append(score)
    my_score = sum(list(map(int, input().split())))
    students.sort()        
    number_to_beat = n - k
    min_score = students[number_to_beat - 1] + 1
    score_required = min_score - my_score
    print('Impossible' if score_required > m else 0 if score_required < 0 else score_required)
