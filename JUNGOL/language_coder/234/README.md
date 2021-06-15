## 234. 함수3 - 형성평가4

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=134&sca=10d0)

1회독: 21.06.02



### my Idea

기본 재귀 형태로 구현하면 중복값 계산으로 인해 최대 깊이 초과 및 시간 초과 문제 발생

배열을 선언해 원소의 값을 가져오는 방식으로 접근해야 해결할 수 있는 문제

### my solution

```python
N = int(input().strip())
# 1. N의 크기에 맞는 배열 만들어 주기 - 해당 인덱스에 저장하겠다
arr = [0 for _ in range(N)]
arr[0] = 1
arr[1] = 2


def recur(n: int) -> int:
    # 1. 종료 조건 설정
    if n == N - 2:
        return arr[-1]
    else:
        arr[n + 2] = arr[n] * arr[n + 1] % 100
        return recur(n + 1)

print(recur(0))
```

배열을 함수 밖에 선언해서 인덱스 값을 가져오는 식으로 설계하여 중복을 없앰



### (틀린 코드)

```python
N = int(input().strip())

def recur(n: int) -> int:
    # 1. 종료 조건 설정
    if n <= 2:
        return n
    else:
        return recur(n - 2) * recur(n - 1) % 100

print(recur(N))
```

시간 초과 발생 

recur(n - 2)와 recur(n - 1)에서 중복하여 두 번 연산되어짐 

이 부분의 중복을 없애자



### 태그

- 재귀