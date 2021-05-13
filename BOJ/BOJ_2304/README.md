## 2304. 창고 다각형

[문제 링크](https://www.acmicpc.net/problem/2304)

1회독: 21.01.20



### Idea

핵심 로직은 지금까지의 가장 큰 값을 저장하고 이와 비교하면서 더 큰 값이 나왔을 때는  

(0) 현재 배열에서 가장 큰 값을 기준으로 좌, 우를 나눈다 

(1) 더 큰 값이 나온 부분 -1 index까지는 저장된 큰 값으로 요소를 넣어준다(pivot) 

(2) 그리고 나서 pivot을 갱신해준다 

(3) 이를 반복한다



### my solution 1

```python
# N: 기둥의 개수
N = int(input())
arr = []

# 1. 기둥 정보 넣기
for _ in range(N):
    l, h = map(int, input().split())
    arr.append((l, h))
# 1-1. 기둥위치에 따라 정렬
arr.sort(key=lambda x : x[0])

ware_house = [0 for _ in range(arr[-1][0] + 1)]

for i in range(N):
    ware_house[arr[i][0]] = arr[i][1]


for i in range(1, N):
    if ware_house[i]:
        ware_house = ware_house[i:]
        break

# 2. 현재 배열에서 max값 찾기
pivot = ware_house.index(max(ware_house))

def left_check(l, r):
    # break 조건
    if l >= r:
        return
    # 1. 왼쪽의 sub_max 값 찾기
    sub_p = ware_house[:r].index(max(ware_house[:r]))
    # 2. sub_p ~ r까지 값 갱신
    for i in range(sub_p, r):
        ware_house[i] = ware_house[sub_p]

    left_check(l, sub_p)

def right_check(l, r):
    # break 조건
    if l >= r:
        return
    # 1. 오른쪽의 sub_max 값 찾기
    sub_p = ware_house[l:].index(max(ware_house[l:])) + l
    # 2. sub_p ~ r까지 값 갱신
    for i in range(l, sub_p):
        ware_house[i] = ware_house[sub_p]

    right_check(sub_p+1, r)
def check(l, p, r):
    left_check(l, p)
    right_check(p+1, r)

    return sum(ware_house)


print(check(0, pivot, len(ware_house) - 1))
```



### my solution 2

```python
def roof(height):
    # 나보다 크거나 같은 것을 만나기 전 인덱스까지는 나의 높이로
    max_height = height.index(max(height))

    # 좌측 시작
    benchmark, result = 0, 0
    for i in range(max_height):
        if height[i] > benchmark:
            benchmark = height[i]
        result += benchmark

    # 우측 시작
    benchmark = 0
    for i in range(len(height)-1, max_height, -1):
        if height[i] > benchmark:
            benchmark = height[i]

        result += benchmark

    result += height[max_height]
    return result

    # 위와 같은 상황이 없다면 나머지들 중에서 가장 큰 높이로 그 전까지는 그 높이로
# [4, 0, 6, 3, 0, 0, 10, 0, 0, 4, 0, 6, 0, 8]

N = int(input())    # 기둥의 개수

location, height = [], []

# 위치와 높이를 두개의 리스트로 받겠다
for i in range(N):
    a, b = map(int, input().split())
    location.append(a)
    height.append(b)

# 위치좌표의 끝의 크기만큼 arr 생성
arr = [0 for _ in range(max(location) + 1)]

# 높이를 arr에 배치
for i in range(len(location)):
    arr[location[i]] = height[i]

print(roof(arr))
```

