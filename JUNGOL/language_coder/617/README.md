## 617. 구조체 - 자가진단5

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=254&sca=10g0)

1회독: 21.06.28



### my solution

```python
arr = []
for _ in range(5):
    temp = input().split()
    name, height = temp[0], int(temp[1])
    arr.append([name, height])

# 1. 작은 순으로 정렬
result = sorted(arr, key=lambda x : x[1])
print(*result[0])
```



### 태그

- 익명함수 lambda
- 리스트