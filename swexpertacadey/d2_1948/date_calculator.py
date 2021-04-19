import sys
sys.stdin = open('input.txt', 'r')

T = int(input())    #test case

for tc in range(1, T+1):

    # 1. dictionary로 월마다 일 수 만들어서 value 접근할 수 있게
    date_limit = {
        1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31,
        9 : 30, 10 : 31, 11: 30, 12 : 31
    }
    # 2. 월, 일 input 받아서 계산
    month_a, day_a, month_b, day_b = map(int, input().split())

    total = 0
    # 3. 첫 달로 들어오는 달의 key로 접근해서 value를 뺀 다음 현재 일자 빼주기
    total += date_limit[month_a] - day_a + 1 # 첫 달의 일 수

    # 4. 중간 월의 일자 더하기
    for month in range(month_a + 1, month_b):
        total += date_limit[month]

    # 5. 마지막 월의 일자 더하기
    if month_a != month_b:
        total += day_b

    print('#{} {}'.format(tc, total))