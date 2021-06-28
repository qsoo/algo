## 197. 구조체 - 형성평가3

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=97&sca=10g0)

1회독: 21.06.28



### Idea

두 개의 직사각형을 포함하는 최소 크기의 직사각형의 좌표를 생각해보면

왼쪽 아래 좌표 (Min$X_1$, Min$Y_1$)

오른쪽 아래 좌표 (Max$X_2$, Max$Y_2$)

즉, 각 index의 요소의 값의 크기를 비교하면 된다



### my solution 1

```python
arr = []
for _ in range(2):
    temp = list(map(int, input().split()))
    arr.append(temp)
# 1. 최소 직사각형의 좌표 (MinX1, MinY1), (MaxX2, MaxY2)
result = [0 for _ in range(4)]

for i in range(4):
    min_temp, max_temp = float('inf'), 0
    # 조건에 맞게 좌표 추출
    if (i < 2 and (arr[0][i] < arr[1][i])) or (i >= 2 and (arr[0][i] > arr[1][i])):
        temp = arr[0][i]
    else:
        temp = arr[1][i]

    result[i] = temp

print(*result)
```

아래 코드에서 중복된 부분 제거하고 조건문을 하나로 합친 것(거의 같다)



### my solution 2

```python
arr = []
for _ in range(2):
    temp = list(map(int, input().split()))
    arr.append(temp)
# 1. 최소 직사각형의 좌표 (MinX1, MinY1), (MaxX2, MaxY2)
result = [0 for _ in range(4)]

for i in range(4):
    min_temp, max_temp = float('inf'), 0
    for j in range(len(arr)):
        # 왼쪽 아래 좌표
        if i < 2:
            if arr[j][i] < min_temp:
                min_temp = arr[j][i]

            result[i] = min_temp
        else:
            if arr[j][i] > max_temp:
                max_temp = arr[j][i]
            result[i] = max_temp

print(*result)
```



### 태그

- 리스트
- 조건문

