## 167. 배열2 - 형성평가8

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=67&sca=10a0)

1회독: 20.12.23



### my solution

```python
arr = [list(map(int, input().split())) for _ in range(4)]

result = []
# 가로 평균
row_avg = []
for i in range(len(arr)):
    temp = sum(arr[i]) // len(arr[i])
    row_avg.append(temp)

result.append(row_avg)

# 세로 평균
col_avg = []
for x in range(len(arr[0])):
    temp = 0
    for y in range(len(arr)):
        temp += arr[y][x]

    col_avg.append(temp // len(arr))

result.append(col_avg)

# 전체 평균
temp = 0
for y in range(len(arr)):
    temp += sum(arr[y])
# unpack 사용을 위해 리스트로 한번 더 감싸줌
result.append([temp // (len(arr) * len(arr[0]))])

for i in range(len(result)):
    print(*result[i])
```



### 태그

- 배열