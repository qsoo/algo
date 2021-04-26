import sys
sys.stdin = open('2382.txt', 'r')


def grouping(y, x, num_and_direct:tuple, M):
    # 1. 4방향 이동에 참고할 리스트 생성
    possible_direction = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    num, direct = num_and_direct

    # 1. 현재지점 초기화
    arr[y][x] = 0
    # 2. 이동한 지점에 값 넣어주기
    new_y = y + possible_direction[direct][0]
    new_x = x + possible_direction[direct][1]

    # 3. 인덱스가 벽에 만나는지 확인
    if new_y == 0 or new_x == 0 or new_y == N-1 or new_x == N-1:
        # 벽에 만나면 방향을 반전시켜준다


for tc in range(1, int(input()) + 1):
    # N: 크기, M: 경과시간, K: 미생물 군집 수
    N, M, K = map(int,input().split())
    arr = [[0] * N for _ in range(N)]

    # 방향은 1, 2, 3, 4 (상, 하, 좌, 우)
    # 1. 인덱스 위치에 튜플형태로(수, 이동방향) 저장 시키기
    for _ in range(K):
        y, x, num, direction = map(int, input().split())
        arr[y][x] = (num, direction)

    # 2. x, y == 0, -1 사방 벽은 미생물에 변화 오는 지점
    # 탐색하면서 1. 벽을 만났니? 2. 군집끼리 만났니 확인
    for y in range(N):
        for x in range(N):
            if arr[y][x] != 0:
                grouping(y, x, arr[y][x], M)
    # 3. 탐색하면서 미생물 군집 발견하면 이동 시키기
