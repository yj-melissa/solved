marks = list(input())
top = -1
cnt = 0
for i in range(len(marks)):
    if marks[i] == '(':    # 여는 괄호라면 top + 1
        top += 1
    
    else:           # 닫는 괄호일 때
        if marks[i-1] == '(':    # 여는 괄호와 연달아 나왔다면 top(쇠막대 개수)만큼 cnt 추가
            cnt += top
            top -=1

        else:
            top -= 1
            cnt += 1     # 쇠막대가 끝났을 때 개수 추가
print(cnt)