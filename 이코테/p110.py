# p110 상하좌우

def check_delta(row, col):
    if (row > 0 and row <= N) and (col > 0 and col <= N):
        return True
    else:
        return False

def move(row, col, d):
    dr = dc = 0
    if d == 'L':
        dc = -1
    elif d == 'R':
        dc = 1
    elif d == 'U':
        dr = -1
    elif d == 'D':
        dr = 1

    if check_delta(row+dr, col+dc):
        return row+dr, col+dc
    else:
        return row, col


import sys
sys.stdin = open('input.txt')

N = int(input())
plan = list(input().split())

row, col = 1, 1     # 시작 좌표 (1,1)

for d in plan:
    row, col = move(row, col, d)

print(row, col)