N = int(input())
members = [list(input().split()) for _ in range(N)]
members = sorted(members, key = lambda x : int(x[0]))
for m in members:
    print(*m)