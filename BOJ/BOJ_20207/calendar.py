# N: 일정 개수, 시작 - 종료
N = int(input())

# index - 365
arr = [0] * 366
# 1 ~ 365 / N : 1000
for i in range(N):  # 1000
    # start point, end point
    a, b = map(int, input().split())    # 365
    for j in range(a, b+1):
        arr[j] += 1

# 1000 * 365 ( N X ) 36만 5천
# arr안에는 겹친 개수들이 들어가 있다

# 코팅지의 높이를 구해서 넓이를 구하기
total = 0
i = 0
while i <= 365: # 365
    # 높이와 너비
    height = 0
    width = 0
    while arr[i]:   # 365
        height = max(arr[i], height)
        width += 1
        i += 1
    i += 1
    # 하나의 직사각형 넓이 최종값에 더해주기
    total += height * width
# 365 * 365
print(total)