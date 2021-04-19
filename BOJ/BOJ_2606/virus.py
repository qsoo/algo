# N: 컴퓨터의 수, E: 연결된 네트워크 수
N = int(input())
E = int(input())

# adjacent_matrix
adj_mat = [[0] * (N+1) for _ in range(N+1)]

for i in range(E):
    a, b = map(int, input().split())
    adj_mat[a][b] = 1
    adj_mat[b][a] = 1

# 방문 check list 생성
visited = [0] * (N + 1)

# BFS 실시
def bfs(start:int) -> int:
    queue = []
    # 1. 직접 연결 찾기
    visited[start] = 1
    for i in range(N + 1):
        if adj_mat[start][i]:
            queue.append((start, i))
            visited[i] = 1

    # 2. bfs 실시
    while queue:
        start, end = queue.pop(0)
        visited[end] = 1

        for i in range(N+1):
            if adj_mat[end][i] and not visited[i]:
                queue.append((end, i))

    # 3. virus computer count
    return sum(visited) - 1

print(bfs(1))



# adjacency matrix
dic={}

# N: 컴퓨터의 수 1: set() ... 형태로 딕셔너리 생성해줌
for i in range(int(input())):
    dic[i+1] = set()

# E: edge 수만큼 연결 {1: {2, 5} ...}
for j in range(int(input())):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)



def dfs(start, dic):
    # start 지점과 연결된 노드들 탐색
    for i in dic[start]:
        # 방문하지 않았다면(리스트 안에 없다면)
        if i not in visited:
            visited.append(i)
            # 연결된 노드로 다시 재귀함수가 작동하기 떄문에 dfs 형태
            dfs(i, dic)
# 방문 check
visited = []
dfs(1, dic)
print(len(visited)-1)

