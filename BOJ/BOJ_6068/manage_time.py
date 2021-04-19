# 1. 인덱스 - 시간, value 걸리는 시간 체크
arr = [0 for _ in range(10000001)]

# 2.n - 수행할 일의 개수 a - 걸리는 시간, b - 끝나는 시간
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    # idx의 val 판별을 위한 변수
    i = 0
    is_can = False
    while i < a:
        # idx 범위 벗어나게 되면 주어진 업무 수행 불가
        if b - i < 0:
            is_can = True
            break
        # 해당 시간에 주어진 업무가 없을 때 => 바로 넣어주기
        if not arr[b - i]:
            arr[b - i] = 1
            i += 1

        # 해당 시간에 주어진 업무가 있을 때 => 주어진 업무 전에 빈 시간까지 이동
        else:
            b -= 1

    if is_can:
        break

# 가능한 시간 구하기
if is_can:
    print(-1)
else:
    print(arr.index(1) - 1)
