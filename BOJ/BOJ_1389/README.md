## 1389. 케빈 베이커의 6단계 법칙

[문제 링크](https://www.acmicpc.net/problem/1389)

1회독: 21.03.03



### Idea

모든 시작점을 기준으로 방문 여부를 체크해서  

(1) 최소값(1에서 시작할 때 다 돌 경우 ... 2... 3.. ...) 

(2) BFS(DFS는 항상 최소 경로를 보장해주는 것이 아니기 때문에 - 하나의 도착지가 아님) 

(3) 백트레킹: 현재까지의 최소 경로보다 커지는 경우 종료



### my solution

```python
def dfs(num: int, k: int):
    # 방문 여부 check
    visited = [0] * (N + 1)

    # 최종 거리 가산
    result = 0
    queue = []
    # 방문 체크
    visited[num] = 1
    queue.append((num, k))
    while queue:
        # 1. 방문하지 않았고 갈 수 있으면 방문
        target, dist = queue.pop(0)
        for i in range(len(arr[target])):
            next = arr[target][i]
            if not visited[next]:
                queue.append((next, dist + 1))
                visited[next] = 1
                # 거리 정보 더해주기
                result += dist + 1
                # backtracking
                if result > min_dist:
                    return float('inf')

    return result


# N: 유저의 수, M: 친구 관계의 수
N, M = map(int, input().split())

# index 바로 1부터 이용하기 위해
arr = [[] for _ in range(N + 1)]
arr[0] = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 1. 모든 유저에 대해 비교
min_dist = float('inf')
result = 0
for i in range(1, N + 1):
    temp_dist = dfs(i, 0)
    if temp_dist < min_dist:
        result, min_dist = i, temp_dist

print(result)
```



### (틀린 코드)

```python
def dfs(num: int, k: int):
    # 방문 여부 check
    visited = [0] * (N + 1)

    # 최종 거리 가산
    result = 0
    stack = []
    # 방문 체크
    visited[num] = 1
    stack.append((num, k))
    while stack:
        # 1. 방문하지 않았고 갈 수 있으면 방문
        target, dist = stack.pop(-1)
        for i in range(len(arr[target])):
            next = arr[target][i]
            if not visited[next]:
                stack.append((next, dist + 1))
                visited[next] = 1
                # 거리 정보 더해주기
                result += dist + 1
                # backtracking
                if result > min_dist:
                    return float('inf')

    return result


# N: 유저의 수, M: 친구 관계의 수
N, M = map(int, input().split())

# index 바로 1부터 이용하기 위해
arr = [[] for _ in range(N + 1)]
arr[0] = 0

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

# 1. 모든 유저에 대해 비교
min_dist = float('inf')
result = 0
for i in range(1, N + 1):
    temp_dist = dfs(i, 0)
    if temp_dist < min_dist:
        result, min_dist = i, temp_dist

print(result)
```

DFS로 설계하게 되면 항상 최단거리를 찾는 게 아니기 때문에 

(방문여부를 체크하기 때문에 항상 최단경로로 가야함) 

이 문제에서는 해결할 수 없음 => BFS로 변경



### 태그

- BFS
- DFS
- 백트래킹