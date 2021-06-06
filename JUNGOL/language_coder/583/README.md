## 583. 함수2 - 자가진단5

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=220&sca=10c0)

1회독: 20.12.30



### my solution 1 

직접 구현

```python
arr = list(map(float, input().split()))

def cal(arr):
    # bubble sort
    # 전체 정렬 탐색 범위
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # 출력 순서에 맞게 위치 변경
    arr[1], arr[2] = arr[2], arr[1]

    # 1. 가장 큰수
    if int(arr[0]) < arr[0]:
        arr[0] = int(arr[0]) + 1
    else:
        arr[0] = int(arr[0])

    # 2. 가장 작은 수
    if arr[1] < int(arr[1]):
        arr[1] = int(arr[1]) - 1
    else:
        arr[1] = int(arr[1])

    # 3. 남은 수
    arr[2] = int(round(arr[2], 0))

    return arr

print(*cal(arr))
```



### my solution 2

math 모듈 이용

```python
import math

arr = list(map(float, input().split()))


def cal(arr):
    arr.sort(reverse=True)
    # 출력 순서에 맞게 변경
    arr[1], arr[2] = arr[2], arr[1]

    arr[0] = math.ceil(arr[0])
    arr[1] = math.floor(arr[1])
    arr[2] = int(round(arr[2], 0))

    return arr

print(*cal(arr))
```



### 태그

- 정렬
- math

