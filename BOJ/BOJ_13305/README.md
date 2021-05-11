## 13305. 주유소

[문제링크](https://www.acmicpc.net/problem/13305)

1회독: 21.01.13



### Idea

현재보다 싼 주유비인 도시가 나오면 지금까지의 주유비 * 지금까지 이동한 거리를 해주면 된다.



### my solution

```python
# N - 도시의 개수
N = int(input())
# arr[0] - 도시간 거리, arr[1] - 도시의 주유비
arr = [list(map(int, input().split())) for _ in range(2)]

total = 0
price = arr[1][0]
for i in range(N-1):
    if arr[1][i] < price:
        price = arr[1][i]
    total += price * arr[0][i]

print(total)
```



### 틀린 코드

```python
# N - 도시의 개수
N = int(input())
# arr[0] - 도시간 거리, arr[1] - 도시의 주유비
arr = [list(map(int, input().split())) for _ in range(2)]

cost = 0

def cal_gas(arr:list):

    global cost

    dist = arr[0]

    # dist가 0이면 탐색 종료
    if len(dist) == 0:
        return cost

    # dist가 1이면 이를 더해주고 종료
    if len(dist) == 1:
        cost += dist[0] * arr[1][0]
        return cost

    # 도착지점은 주유할 필요없다
    city = arr[1][:-1]

    # 1. 해당 이동구간 중 가장 기름비가 싼 지역 찾기
    target_idx = city.index(min(city))
    # 2. 해당 지점(K)부터 도착지까지의 거리만큼 주유비 소모
    cost += sum(dist[target_idx:]) * city[target_idx]
    # 3. 탐색한 지점 제외하고 새 탐색 범위 설정
    arr = [dist[:target_idx], city[:target_idx]]
    return cal_gas(arr)


print(cal_gas(arr))
```

해당 구간 중 가장 싼 가격의 도시에서 충전하고 

그 전 구간에서도 마찬가지로 진행한다고 생각하고 DP로 구현 

(1) 이동구간 중 가장 싼 지역 찾는다 

(2) 이동구간(K)부터 도착지까지의 거리만큼 주유를 해서 이동 

(3) 이를 첫번째 index(0)까지 반복 수행 

(결과) => 메모리 초과



```python
import sys
sys.setrecursionlimit(10**9)

# N - 도시의 개수
N = int(input())
# arr[0] - 도시간 거리, arr[1] - 도시의 주유비
arr = [list(map(int, input().split())) for _ in range(2)]

cost = 0

def cal_gas(idx:int):

    global cost

    # dist가 0이면 탐색 종료
    if len(arr[0][:idx]) == 0:
        return cost

    # dist가 1이면 이를 더해주고 종료
    if len(arr[0][:idx]) == 1:
        cost += arr[0][0] * arr[1][0]
        return cost

    # 도착지점은 주유할 필요없다
    # 1. 해당 이동구간 중 가장 기름비가 싼 지역 찾기
    target_idx = arr[1][:idx - 1].index(min(arr[1][:idx - 1]))
    # 2. 해당 지점(K)부터 도착지까지의 거리만큼 주유비 소모
    cost += sum(arr[0][target_idx:idx]) * arr[1][target_idx]
    # 3. 탐색한 지점 제외하고 새 탐색 범위 설정
    return cal_gas(target_idx)


print(cal_gas(len(arr[1]) - 1))
```

1번의 해결법에 재귀 깊이를 늘려주고 index를 탐색해서 찾을 수 있는 방식으로 구현했으나 

시간 초과 발생(메모리 문제는 해결했지만 결론적으로는 시간이 많이 걸린다는 뜻!)