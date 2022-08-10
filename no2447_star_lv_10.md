#### 백준 no. 2447 별찍기 Lv. 10

08/10)

- 체감 난이도 급상승.. 재귀 형태를 이용해서 조건에 맞게 패턴을 반복시켜야한다.

- 기본 모양을 반영한 행렬을 만들어 놓고, 그걸 재귀함수로 반복시키면 되겠다!라는 생각을 했을 때까지는 만족했는데, 그걸 반복을 못 시키고 있다. 이걸 어떻게 반복 시켜야하지..?

- 현재까지 작성한 코드
  
  ```python
  def rec(N):
      pttn = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
      n = N // 3
  
      if n <= 1:
          for i in range(3):
              for j in range(3):
                  p = pttn[i][j]
                  if p :
                      print('*', end = '')
                  else :
                      print(' ', end = '')
  
      else:
          for i in range(n):
              for j in range(n):
                  rec(n-1)
              n -= 1
  ```
