## 579. 함수2 - 자가진단1

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=216&sca=10c0)

1회독: 21.12.29



### my solution

```python
n = int(input())
arr = list(map(int, input().split()))

def bubble_sort(arr:list) -> list:
    # 1. 정렬할 길이 탐색 범위
    for i in range(len(arr)-1, 0, -1):
        # 2. 이 전단계에서 비교했던 값들을 다시 비교할 때 사용
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(*bubble_sort(arr))
```





### 태그

- 정렬
- 거품 정렬
- bubble sort