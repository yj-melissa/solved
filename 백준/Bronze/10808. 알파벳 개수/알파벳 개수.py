alphabets = 'abcdefghijklmnopqrstuvwxyz'
N = len(alphabets)
cnt_list = [0] * N
S = input()

for idx in range(N):
    for s in S:
        if alphabets[idx] == s:
            cnt_list[idx] += 1

print(*cnt_list)
