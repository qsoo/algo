## 1949. 등산로 조성

[문제링크](https://zzu.li/02cyt)

1회독: 20.12.02



### idea

가장 높은 봉우리 높이 h를 찾는다 

높이가 h인 모든 칸에서 시작해본다 

현재 칸에 인접한 낮은 칸으로 이동한다. 

낮지 않은 칸은 , 높이 차이가 K보다 작고 깍는 횟수가 남아있으면 이동한다. 

이미 등산로에 포함된 칸을 깍지 않도록 한다. 

깎은 칸 방향 탐색 후 다른 방향을 탐색할 때 원래 높이를 복원한다 각 칸에 들어갈 때마다 가장 긴 등산로와 비교해 최대길이를 갱신한다.

*등산로 여부를 방문여부 체크*

*깎을 때 현재 위치보다 1작게 만드는게 가장 유리 - 다다음번까지 생각을 안해도 된다*

*(좌표, 깎았는지 여부, 길이) 를 넘겨주면서 DFS, BFS 진행*



- my solution

```python
def search_hiking(sx, sy):
    # 등산로 길이
    global long

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    queue = []
    queue.append((sx, sy, 1))

    while queue:
        sx, sy, cnt = queue.pop(0)

        # 등산로의 길이
        for i in range(4):
                new_y = sy + dy[i]
                new_x = sx + dx[i]
                # 인덱스 범위 탐색
                if 0 <= new_x < N and 0 <= new_y < N:
                    # 이 전의 높이와 현재의 높이 비교
                    before = arr[sy][sx]
                    now = arr[new_y][new_x]

                    if before > now:
                        queue.append((new_x, new_y, cnt+1))

    # 가장 긴 길이 찾기
    if long < cnt:
        long = cnt

for tc in range(1, int(input()) + 1):
    # N: 지도의 크기, K: 최대 공사 가능 깊이
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_height = 0
    max_height_list = []
    # 최대 높이의 크기 구하기
    for y in range(N):
        temp = max(arr[y])
        if max_height < temp:
            max_height = temp

    # 최대 높이의 인덱스 구하기 - start 지점
    for y in range(N):
        for x in range(N):
            if arr[y][x] == max_height:
                max_height_list.append((x, y))

    # 등산로 길이 비교 변수
    long = 0
    # 2. 해당 지점에서 갈 수 있는 가장 긴 길이 찾기
    for i in max_height_list:
        sx, sy = i
        search_hiking(sx, sy)

    # 3. K의 높이만큼 봉우리를 낮췄을 때 갈 수 있는 길 탐색
    temp = 1

    while temp <= K:
        for y in range(N):
            for x in range(N):
                # 제일 높은 봉우리면 넘어가고
                arr[y][x] = arr[y][x] - temp
                # 갱신한 다음 최대 길이 찾기
                for i in max_height_list:
                    sx, sy = i
                    search_hiking(sx, sy)
                # 다시 되돌리기
                arr[y][x] = arr[y][x] + temp

        # for문이 끝나면 temp 값 증가
        temp += 1

    print('#{} {}'.format(tc, long))
```

