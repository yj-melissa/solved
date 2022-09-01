notes = list(map(int, input().split()))
ref = list(enumerate('cdefgabC', start=1))

asc_cnt = des_cnt = 0

for idx, note in ref:
    if idx == notes[idx-1]:
        asc_cnt += 1
    elif 9-idx == notes[idx-1]:
        des_cnt += 1
    else:
        print('mixed')
        break
else:
    if asc_cnt == 8:
        print('ascending')
    else:
        print('descending')