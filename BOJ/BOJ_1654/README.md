## 1654. 랜선 자르기

[문제링크](https://www.acmicpc.net/problem/1654)



### Idea

이진탐색(Binary Search) 

이진탐색을 위한 전제 조건 

- *데이터가 정렬되어 있어야 한다* 

(오름차순 정렬이라 가정하면) 

left(Min value) , middle, right(Max value) 이라고 가정했을 때 

1. 중간 값과 찾고자하는 값을 비교한다 
2. middle < target ⇒ 배열의 우측으로 이동하여 반복 수행 
3. middle > middle ⇒ 배열의 좌측으로 이동하여 반복 수행 
4. 값을 찾을 때까지 반복수행  

*재귀로 구현하는 방법과 반복문으로 구현하는 방법 존재!*



```python
# 1. 재귀로 구현
def binary_search(start:int, end:int, target:int=0):
    # 0. 종료 조건은 start > end일 때:
    cnt = 0
    mid = (start + end) // 2
    target = mid
    if start > end:
        return target

    for i in range(len(arr)):
        cnt += arr[i] // mid

    # 조건을 만족하면 더 큰 값 찾기
    if cnt >= N:
        start = mid + 1
    # 조건을 만족하지 못하면 더 작은 값 찾기
    else:
        end = mid - 1

    return binary_search(start, end, target)

# K: 이미 가지고 있는 랜선의 개수, N: 만들어야되는 랜선의 개수
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
print(binary_search(1, max(arr)))

# 2. while문 이용
# start를 0으로 지정하면 zerodivisionError 발생 가능 : start, end = 0, 1 일 때
start, end = 1, max(arr)
# 찾고자하는 길이의 값
target = 0
# 오른쪽 가르키는 인덱스가 왼쪽보다 작아지면 검색 종료
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in arr:
        cnt += line // mid

    # mid < target 우측 탐색 실시 == start <- mid + 1
    if cnt >= N:
        start = mid + 1
        target = mid
    # mid > target 좌측 탐색 실시 == end <- mid - 1
    else:
        end = mid - 1

print(target)
```



#### (실패 코드)

```python
# K: 이미 가지고 있는 랜선의 개수, N: 만들어야되는 랜선의 개수
K, N = map(int, input().split())
li = list(int(input()) for _ in range(K))

# 1. 전체합을 구한다
li_sum = sum(li)
# 1-1. 추후 편의를 위해 내림차순으로 정렬
li.sort(reverse=True)

# 1. 전체합으로 구했을 때 N <= 를 만족하는 가장 긴 길이
temp = li_sum // N

result_li = [li_sum]
while len(result_li) != len(li):
    # 2. 가장 긴 길이를 빼서 개수를 다시 구한다
    for i in range(len(li)):
        # 저장된 길이를 빼서 다시 뺀 다음 넣기
        li_sum = result_li.pop()
        result_li.append(li[i])
        # 2-1. 현재의 합에서 가장 긴 길이 빼서 저장 - 마지막까지
        if li_sum != li[i]:
            li_sum -= li[i]
            result_li.append(li_sum)
        # 2-2. 현재까지 나눠진 원소들에서 조건 만족하는 개수 비교
        while True:
            # 만들 수 있는 개수(N) 비교 저장할 변수
            cnt = 0
            for j in range(len(result_li)):
                cnt += result_li[j] // temp

            # 2-3. 조건 만족하는지 확인
            if cnt >= N:
                break
            else:
                temp -= 1

print(temp)
```

(1) 가지고 있는 랜선들의 총합으로 조건을 만족하는 가장 큰 길이 추출
(2) 가장 큰 수부터 떨어져 나오게 해서 (802, 1703)등으로 

이 때 조건을 만족하는 가장 큰 길이를 구해가면서
(3) 주어진 K개로 다 쪼개질 때 만족하는 N의 길이가 가장 긴 길이이다.

=> 구조를 설계한대로 코드를 짜니 시간초과 발생

