## 1249. 보급로

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD&categoryId=AV15QRX6APsCFAYD&categoryType=CODE&problemTitle=%EB%B3%B4%EA%B8%89%EB%A1%9C&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)

1회독: 20.11.03



### Idea

칸을 기준으로 높이가 낮을 때 (즉, 나보다 높아서 기준점보다 위로 올라가는 경우가 없다) 

정보를 지나가면서 누적하면서 결과값을 도출하게 되면 되는 문제 - 다익스트라 알고리즘 이용(최소 비용)



### my solution

```python
def dijkstra(sx, sy):
    # route, weight 담을 배열 생성
    queue = []
    cost[0][0] = 0
    queue.append((0,0))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        new_x, new_y = queue.pop(0)
        # 상하좌우 이동
        for i in range(4):
            # next 지점
            next_x = new_x + dx[i]
            next_y = new_y + dy[i]
            # out of index 방지
            if 0 <= new_x < N and 0 <= new_y < N:
                # 복구 시간 확인
                time = arr[new_y][new_x]
                # 가지 않았거나: 아직 inf, 덜 쓰고 갈 수 있다면: 이전 부터 왔을 때
                if cost[new_y][new_x] + time < cost[next_y][next_x]:
                    queue.append((next_x, next_y))
                    # 작은 값으로 갱신
                    cost[next_y][next_x] = min(cost[next_y][next_x], cost[new_y][new_x] + time)


    return


for tc in range(1, int(input()) + 1):
    # 배열의 크기
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 비용 그래프
    cost = [[float('inf')] * (N + 1) for _ in range(N+1)]

    dijkstra(0, 0)

    print('#{} {}'.format(tc, cost[N-1][N-1]))
```



### 태그

- 다익스트라 알고리즘
- 백트레킹
- 최소신장트리