## Bubble Sort

- 정렬



#### Idea

> swap을 이용해서 뒤에서부터 앞으로 정렬을 진행한다



오름차순으로 정렬한다고 가정했을 때

1. 배열의 처음부터 끝까지 양 옆의 값을 비교해가면서 큰 값을 오른쪽으로 이동
2. 1회 반복이 완료되면 배열에서 가장 큰 값이 배열의 가장 맨 끝(오른쪽)에 위치
3. 마지막 원소는 정렬이 되었기 때문에 탐색하는 배열의 크기를 하나씩 줄여가면서 반복 수행



시간 복잡도 = $O({n}^2)$



Code

```python
# 내림차순 기준
def bubble_sort(arr:list) -> list:
    # 1. 정렬할 길이 탐색 범위
    for i in range(len(arr)-1, 0, -1):
        # 2. 이 전단계에서 비교했던 값들을 다시 비교할 때 사용
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
```

