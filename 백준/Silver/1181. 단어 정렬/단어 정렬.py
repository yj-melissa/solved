N = int(input())
words = [input() for _ in range(N)]

words = list(set(words))        # 중복 제거
words.sort()
words.sort(key = lambda x: len(x))

for word in words:
    print(word)