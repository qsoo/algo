import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # test case

for tc in range(1, T + 1):
    iteration = int(input())    # 시행 수
    arr = [list(map(int, input().split())) for _ in range(iteration)]

    # 0. 속도, 이동거리 변수 설정
    velocity, distance = 0, 0

    # 1. arr[y][0] 탐색해서 무슨 행동인지 확인
    for y in range(len(arr)):
        # 1-1. 가속일 때 조건
        if arr[y][0] == 1:
            velocity += arr[y][1]   # 가속도 부여
            distance += velocity
        # 1-2. 감속일 때 조건
        elif arr[y][0] == 2:

            # 감속이 클 경우에는 velocity = 0
            if arr[y][1] > velocity:
                velocity = 0
            else:
                velocity -= arr[y][1]
                distance += velocity

        # 1-3. 현재 속도 유지
        if arr[y][0] == 0:
            distance += velocity

    print('#{} {}'.format(tc, distance))