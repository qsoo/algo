## 233. 함수3 - 형성평가3

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=133&sca=10d0)

1회독: 21.06.01



### my solution 1

```python
N, M = map(int, input().split())

def recur(n: int, arr:list, sumVal: int):
    # 1. 종료조건
    if n == N:
        if sumVal == M:
            # 2. 출력 조건
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):

            if sumVal + i > M or (N - n) * 6 < M - (sumVal + i):
                break
            recur(n + 1, arr + [i], sumVal + i)
        return

recur(0, [], 0)
```

가지치기를 두 번 해줘야 하는 문제 

(1) 종료 조건인 총 합(M)까지 나오는 조건 

(2) 해당 주사위 숫자부분에서 이미 M보다 커졌을 때 

(3) 지금 이후의 시행에서 모두 6이 나와도 M보다 작을 때



### my solution 2

```python
N, M = map(int, input().split())
 
arr = [0 for _ in range(N)]
 
def recur(n: int, total: int):
    # 1. 종료조건
    if n == N:
        if not total:
            # 2. 출력 조건
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            arr[n] = i
            if total - i < 0 or (N - n) * 6 < total:
                break
            recur(n + 1, total - i)
        return
 
recur(0, M)
```

배열을 함수 외부에 선언해서 좀 더 시간 단축(약 1/2)



### (틀린 코드)

```python
N, M = map(int, input().split())

def recur(n: int, arr: list, sumVal: int):
    # print(n, m, arr)
    # 1. 종료 조건 추가 - 값이 더 클 때
    if sumVal > M:
        return
    # 1. 종료조건
    elif n == N:
        # 2. 출력 조건
        if sumVal == M:
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            arr.append(i)
            recur(n + 1, arr, sumVal+i)
            arr.pop(-1)

recur(0, [], 0)
```

시간 초과 발생 최초 구조에서 

(1) M 값 넘겨주지 않기 

(2) 합을 구하는 과정 변경 을 했지만 시간초과 발생 - 6개 통과



```python
N, M = map(int, input().split())

def recur(n: int, arr: list, sumVal: int):
    # print(n, m, arr)
    # 1. 종료 조건 추가 - 값이 더 클 때
    if sumVal > M:
        return
    # 1. 종료조건
    elif n == N:
        # 2. 출력 조건
        if sumVal == M:
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            recur(n + 1, arr + [i], sumVal+i)

recur(0, [], 0)
```

(3) 배열을 넘겨줄 때 append, pop 과정 삭제 - 8개 통과 

6번 8 43일 때 시간 초과 나는 것을 확인



```python
N, M = map(int, input().split())

def recur(n: int, arr: list, sumVal: int):
    # 1. 종료조건
    if n == N:
        if sumVal == M:
            # 2. 출력 조건
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            if sumVal + i > M:
                break
            recur(n + 1, arr + [i], sumVal+i)
        return

recur(0, [], 0)
```

시간 좀 더 줄인 것



### 태그

- 재귀