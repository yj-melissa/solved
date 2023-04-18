grade_table = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
score_total = 0             # 학점 * 과목평점 합
credit_total = 0            # 학점 총합
for _ in range(20):
    _, credit, grade = input().split()
    if grade == 'P':
        continue
    score_total += float(credit) * grade_table[grade]
    credit_total += float(credit)
print(score_total / credit_total)