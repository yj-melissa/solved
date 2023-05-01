N = int(input())
num = 666             # 제일 작은 종말의 수
answer = 0              # 답
while N > 0:
    if '666' in str(num):
        N -= 1
        answer = num
    num += 1
print(answer)