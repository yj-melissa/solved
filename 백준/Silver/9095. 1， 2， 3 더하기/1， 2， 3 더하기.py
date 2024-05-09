T = int(input())
for _ in range(T):
    n = int(input())
    arr = [0] * (n + 1)

    for i in range(1, n + 1):
        if i == 1:
            arr[1] = 1
        elif i == 2:
            arr[2] = 2
        elif i == 3:
            arr[3] = 4
        else:
            arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

    print(arr[n])