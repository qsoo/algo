import sys
sys.stdin = open("input.txt", "r")

T = int(input())    # test case

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 배열의 길이
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))

    result = [] # 요소들의 합의 값 저장할 빈 리스트 생성
    # 0. M > N
        # 1. 요소에 접근해서 곱한다
    multiply = 0    # 요소들의 곱의 합

    # 2. 인덱스를 변수로 생성해서 접근
    a = b = 0   # a,b 리스트의 인덱스 변수

    if M > N:
        # 3. N이 작기 때문에 N을 이용한 순환문 생성
        while b <= (M - N):
            for n in range(N):
                multiply += list_a[n] * list_b[b + n]

            result.append(multiply)
            multiply = 0
            b += 1

    elif N >= M:
        while a <= (N - M) :
            for m in range(M):
                multiply += list_a[a + m] * list_b[m]

            result.append(multiply)
            multiply = 0
            a += 1

    print("#{} {}".format(tc, max(result)))