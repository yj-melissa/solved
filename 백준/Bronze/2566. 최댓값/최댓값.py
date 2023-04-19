arr = [list(map(int, input().split())) for _ in range(9)]
max_num = max_row = max_col = 0

for r in range(9):
    for c in range(9):
        if arr[r][c] > max_num:
            max_num = arr[r][c]
            max_row, max_col = r, c
print(max_num)
print(max_row+1, max_col+1)