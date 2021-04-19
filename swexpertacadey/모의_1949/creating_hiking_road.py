import sys
from pprint import pprint
sys.stdin = open('1949.txt', 'r')

# 1. 스타트 위치 (가장 높은 봉우리 찾는다)
# 2. 해당 지점에서 갈 수 있는 길이 가장 긴 것을 찾는다
# 3. k의 크기만큼 봉우리 높이를 낮춰서 갈 수 있는 길을 찾는다
# 4. 높이를 낮췄을 때 갈 수 있는 길이가 길어진다면 최대 길이를 갱신해준다


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