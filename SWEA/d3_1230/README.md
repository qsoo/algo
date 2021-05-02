## 1230. 암호문3

[문제링크](https://zzu.li/wts1z)

1회독: 20.11.11



### Idea

시간당 이동할 수 있는 칸 수가 하나씩이기 때문에 BFS를 통해 탐색을 하면 간결하게 구현이 가능 다만 유의할 점은 출발지점에서 다음지점으로 이동할 때 파이프의 모양에 따라 갈 수 있는 부분이 있고 못 가는 부분이 있기 때문에 이를 break할 수 있게 만들어줘야함



- my solution

```python
def find_pipe(sy, sx):
    # 번호 확인
    target = arr[sy][sx]
    # pipe dictionary에서 파이프 모양 확인
    # pipe - 0인 경우 분기해줘야 함
    if not target:
        return 0
    else:
        return pipe[target]


def check(x, y):
    # 파이프가 없는 공간일 때 조건 추가
    if 0 <= y < N and 0 <= x < M and arr[y][x] and not visited[y][x]:
        return True
    else:
        return False

# 이 전 파이프에서는 올 수 있었는데 모양이 이어지지 않았을 때 걸러주기
def check_pipe(direction: int, pipe: tuple):
    # direction의 정보를 바탕으로 pipe가 이어질 수 있는지 판별
    if direction == 0:
        target = 1
    elif direction == 1:
        target = 0

    elif direction == 2:
        target = 3
    elif direction == 3:
        target = 2

    if target in pipe:
        return True
    else: return False

def bfs(sy, sx, depth):
    global cnt

    queue = []
    queue.append((sy, sx, depth))
    # 시작지점 방문 체크
    visited[sy][sx] = 1
    while queue:
        sy, sx, depth = queue.pop(0)

        # prunning - 경과시간이 같아질 때
        if depth == L:
            break
        # 먼저 파이프 모양이 무엇인지 판별하여 이동할 수 있는 지점 확인
        pipe = find_pipe(sy, sx)
        # 0인 경우: pipe가 해당 지점에 없을 때 밑에 진행할 필요가 없다
        if not pipe:
            continue

        for i in pipe:
            new_y = sy + dy[i]
            new_x = sx + dx[i]

            # i 정보를 가지고 - 이전 어디서 왔냐 확인
            # 이후 정보에 내가 그 방향에서 올 수 있는 파이프?
            if check(new_x, new_y):
                next_pipe = find_pipe(new_y, new_x)
            else:
                continue
            # 범위 확인
            if check_pipe(i, next_pipe):
                visited[new_y][new_x] = 1
                queue.append((new_y, new_x, depth + 1))
                cnt += 1

    return


for tc in range(1, int(input()) + 1):
    # N * M : 지하터널 크기 / [R, C]: 탈출 지점 / L - 소요시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 파이프 딕셔너리 생성
    pipe = {
        1: (0, 1, 2, 3),
        2: (0, 1),
        3: (2, 3),
        4: (0, 3),
        5: (1, 3),
        6: (1, 2),
        7: (0, 2)
    }

    # 방문여부 확인
    visited = [[0] * M for _ in range(N)]
    # 최종 이동 범위 확인
    cnt = 1

    bfs(R, C, 1)

    print('#{} {}'.format(tc, cnt))
```



`BFS`

`백트래킹`

