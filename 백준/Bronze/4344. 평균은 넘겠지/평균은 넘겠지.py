C = int(input())

for _ in range(C):
    tc = list(map(int, input().split()))
    students, scores = tc[0], tc[1:]
    avg = sum(scores) / students
    over_avg = 0
    for s in scores:
        if s > avg:
            over_avg += 1
    print(f'{over_avg/students*100:.3f}%')