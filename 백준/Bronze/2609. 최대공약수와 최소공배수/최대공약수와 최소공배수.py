n1, n2 = map(int, input().split())

# 최대 공약수
GCD = 1
for i in range(min(n1, n2), 1, -1):
    if n1 % i == 0 and n2 % i == 0:
        GCD = i
        break

# 최소 공배수
LCM = (n1 * n2) // GCD

print(GCD)
print(LCM)