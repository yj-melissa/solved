S = input()
N = len(S)
# 접미사 추출
suffix = []
for i in range(N):
    res = ''
    for j in range(i, N):
        res += S[j]
    suffix.append(res)
suffix.sort()
for s in suffix:
    print(s)