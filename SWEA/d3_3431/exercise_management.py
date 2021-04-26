for tc in range(1, int(input()) + 1):
    # L: low, U: high, X: 실제 운동 시간
    L, U, X = map(int, input().split())

    # 시간 초과인지 아닌지 판별
    if L <= X <= U:
        result = 0
    elif U < X:
        result = -1
    else:
        result = L - X

    print('#{} {}'.format(tc, result))