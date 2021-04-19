# N - 도시의 개수
N = int(input())
# arr[0] - 도시간 거리, arr[1] - 도시의 주유비
arr = [list(map(int, input().split())) for _ in range(2)]

total = 0
price = arr[1][0]
for i in range(N-1):
    if arr[1][i] < price:
        price = arr[1][i]
    total += price * arr[0][i]

print(total)


'''
import sys
sys.setrecursionlimit(10**9)

def cal_gas(idx:int):

    global cost

    # dist가 0이면 탐색 종료
    if len(arr[0][:idx]) == 0:
        return cost

    # dist가 1이면 이를 더해주고 종료
    if len(arr[0][:idx]) == 1:
        cost += arr[0][0] * arr[1][0]
        return cost

    # 도착지점은 주유할 필요없다
    # 1. 해당 이동구간 중 가장 기름비가 싼 지역 찾기
    target_idx = arr[1][:idx - 1].index(min(arr[1][:idx - 1]))
    # 2. 해당 지점(K)부터 도착지까지의 거리만큼 주유비 소모
    cost += sum(arr[0][target_idx:idx]) * arr[1][target_idx]
    # 3. 탐색한 지점 제외하고 새 탐색 범위 설정
    return cal_gas(target_idx)


print(cal_gas(len(arr[1]) - 1))
'''