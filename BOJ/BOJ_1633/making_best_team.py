# 시작 포인트를 잡아줘야 한다 - 계속해서 비교하면서 나아가기 때문에
arr = [[0, 0]]

# 입력 받는 방법 1 - 가장 속도 느림
while True:
    try:
        a, b = map(int, input().split())
        arr.append((a, b))
    except:
        break

'''
import sys
# 입력 받는 방법 2
for line in sys.stdin:
    if line =='\n':
        break
    line = tuple(map(int, line.split()))
    arr.append(line)


# 입력 받는 방법 3
while True:
    line = sys.stdin.readline().split()  
    print(line)
    if not line:
        break
    arr.append(list(map(int, line)))
'''

# 우측부터 len(arr) - 전체 참가자 수 -> 백색 돌의 수 -> 흑색 돌의 수
# 모든 경우의 수를 기록한다
DP = [[[0 for _ in range(16)] for _ in range(16)] for _ in range(len(arr))]

# 전체 테스트 중 안 넣는 경우, 검은색으로 넣는 경우, 흰색으로 넣는 경우 - 3가지 고려
for i in range(1, len(arr)):
    for j in range(16):
        for k in range(16):
            # 안넣었을 때
            DP[i][j][k] = DP[i-1][j][k]
            # white로 넣었을 때
            if j > 0:
                DP[i][j][k] = max(DP[i-1][j-1][k] + arr[i][0], DP[i][j][k])
            # black로 넣었을 때
            if k > 0:
                DP[i][j][k] = max(DP[i-1][j][k-1] + arr[i][1], DP[i][j][k])

print(DP[len(arr)-1][15][15])



