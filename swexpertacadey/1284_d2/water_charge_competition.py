import sys
sys.stdin = open("input.txt", "r")

T = int(input())    # test case

for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    '''
    P : A사의 리터당 요금
    Q : B사의 기본 요금
    R : 월간 사용량 기준(리터) - 이하면 기본요금만 청구
    S : B사의 리터당 추가요금
    W : 한달 사용 수도의 양
    '''

    bill_a, bill_b = 0, 0   # A, B사의 요금

    # 1. A사 요금
    bill_a = P * W

    # 2. B사 요금
    # 2-1. R 미만 = 기본요금
    if W < R:
        bill_b = Q

    else:
        bill_b = Q + ((W - R)*S)

    result = 0
    result = min(bill_a, bill_b)

    print('#{} {}'.format(tc, result))