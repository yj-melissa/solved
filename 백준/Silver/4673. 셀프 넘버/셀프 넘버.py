num_list = [0] * 10001
answer = []

for i in range(1, 10001):
    if num_list[i] == 0:
        answer.append(i)
    gen_num = i
    while i > 0:
        gen_num += i % 10
        i //= 10
    if gen_num <= 10000:
        num_list[gen_num] = 1

for n in answer:
    print(n)