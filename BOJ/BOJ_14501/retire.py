# 현재일자, 지금까지의 합
def dfs(day, total):
    # 종료조건 - 퇴사날 되었다
    if day >= N:
        global income
        if income < total:
            income = total
        return

    # 1. 현재시점 상담한다
    if day + arr[day][0] <= N:
        dfs(day + arr[day][0], total + arr[day][1])
    # 2. 상담안하고 다음으로 넘어간다
    if day + 1 <= N:
        dfs(day + 1, total)


# N: 일하는 일수 - index
N = int(input())
# (걸리는 일 수, 버는 금액)
arr = [tuple(map(int, input().split())) for _ in range(N)]

# 최대수익
income = 0
# 1. 시작지점을 탐색하면서 최대 금액 확인
dfs(0, 0)

print(income)