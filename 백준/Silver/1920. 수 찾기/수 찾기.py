N = int(input())
A_list = list(map(int, input().split()))
M = int(input())
find_list = list(map(int, input().split()))     # 찾을 수 목록

intersection = set(A_list) & set(find_list)           # 교집합

for f in find_list:
    if f in intersection:
        print(1)
    else:
        print(0)
        