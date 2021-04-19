N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

from pprint import pprint
pprint(arr)
print()

# 1. 구역 설정(DFS, while) - 섬 번호 부여
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 방문여부 체크
visited = [[False] * M for _ in range(N)]
# beach = [[False] * M for _ in range(N)]
# 해당 섬 번호
area = 1
for y in range(N):
    for x in range(M):
        if arr[y][x] and not visited[y][x]:
            visited[y][x] = True
            # 섬 번호 첫 부여
            arr[y][x] = area
            stack = [(y, x)]
            # dfs 도는 동안 모두 같은 섬 지역
            while stack:
                y, x = stack.pop()
                for i in range(4):
                    new_y, new_x = y + dy[i], x + dx[i]
                    if 0 <= new_y < N and 0 <= new_x < M and not visited[new_y][new_x]:
                        if arr[new_y][new_x]:
                            visited[new_y][new_x] = True
                            arr[new_y][new_x] = area
                            stack.append((new_y, new_x))

            area += 1

pprint(arr)
# pprint(visited)

# 2. 섬 다리의 비용 계산
cost = [[float('inf')] * area for _ in range(area)]
# 다리 놓는 지점 확인
for y in range(N):
    for x in range(M):
        if not visited[y][x]:
            start = arr[y][x]
            for i in range(4):
                cnt = 0
                while True:
                    y, x = y + dy[i], x + dx[i]
                    if 0 <= y < N and 0 <= x < M and not arr[y][x]:
                        cnt += 1
                    # 다리 짓기 끝남
                    else:
                        break

                # 최종 비용 확인
                if 0 <= y < N and 0 <= x < M and arr[y][x] and cnt >= 2:
                    end = arr[y][x]
                    cost[start][end] = cost[start][end] = min(cnt, cost[start][end])

print(cost)

