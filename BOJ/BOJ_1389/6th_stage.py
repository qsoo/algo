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
