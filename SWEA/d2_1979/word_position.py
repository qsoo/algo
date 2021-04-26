import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    # test case 수

for tc in range(1, T + 1):
    # N => N X N 배열 / K = word length
    N, K = map(int, input().split())
    # 2차원 배열로 input 받기
    arr = list([int(x) for x in input().split()] for y in range(N))

    total_row, total_col = 0, 0 # length
    result = 0  # 최종 들어갈 수 있는 개수
    # point : 연속 / 0을 만나면 reset

    # case 1: 앞부터 세다가 1만났고 이게 연속되서 K랑 길이가 같아지며 그 다음은 0
    for y in range(N):  # column
        total_row = 0   # initializing
        total_col = 0
        for x in range(N): # row
            # 행 탐색 케이스
            if arr[y][x]:
                total_row += 1
                # total_row == K인데 뒤에 1이 나오는 case 걸러주기
                if total_row == K and x < N - 1 and arr[y][x + 1] != 1:
                    result += 1

                elif total_row == K and x == N - 1:
                    result += 1
            # 0을 만났을 때
            elif arr[y][x] == 0:
                total_row = 0

            # 열 탐색 케이스
            if arr[x][y]:
                total_col += 1
                # total_row == K인데 뒤에 1이 나오는 case 걸러주기
                if total_col == K and x < N - 1 and arr[x + 1][y] != 1:
                    result += 1

                elif total_col == K and x == N - 1:
                    result += 1
            # 0을 만났을 때
            elif arr[x][y] == 0:
                total_col = 0

    print('#{} {}'.format(tc, result))