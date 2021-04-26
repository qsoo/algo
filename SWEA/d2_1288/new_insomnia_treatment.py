import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())    # test case

for tc in range(1, T+1):
    N = int(input()) # 계산을 위해 먼저 int로 생성

    # 1. 비교할 정답 set 생성(0 ~ 9)
    solution_set = set(str(i) for i in range(0, 10))
    result_set = set()  # input 요소를 넣을 세트

    # 2. input을 set으로 만들어서 배수마다 저장
    i = 1   # 배수 옵션
    total = 0   # 결과값 str 저장
    while solution_set != result_set:
        total = N * i
        result_set.update(str(total))
        if result_set != solution_set:
            i += 1

    else:
        print('#{} {}'.format(tc, i*N))
