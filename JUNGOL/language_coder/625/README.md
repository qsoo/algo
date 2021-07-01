## 625. 포인터 - 자가진단7

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=262&sca=10h0)

1회독: 21.07.01



### my solution 1

```python
input()
arr = list(map(int, input().split()))
arr.sort(reverse=True)
print(*arr)
```

파이썬 빌트인 정렬을 이용한 숏 코딩



### my solution 2

```python
input()
arr = list(map(int, input().split()))

def bubble_sort(arr:list, k:int)-> list:
    # 0. 종료 조건
    if k == 1:
        return arr
    # 1. 첫 요소 맨 뒤까지 비교하면서 이동
    for i in range(0, k-1):
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return bubble_sort(arr, k - 1)

print(*bubble_sort(arr, len(arr)))
```

거품 정렬을 이용(가장 작은 값이 맨 뒤에 순차적으로 앞으로 쌓이게 된다)



### 태그

- 정렬