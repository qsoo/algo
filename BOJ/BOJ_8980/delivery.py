# N: 마을 수 C: 용량
N, C = map(int, input().split())

arr = []
# 보내는 박스 정보의 양
M = int(input())
for _ in range(M):
    # 시작 -> 도착, 택배량
    start, end, amount = map(int, input().split())
    # 1. 택배들 도착 정보 리스트에 저장(2차원 배열)
    temp = list(0 for _ in range(N + 1))

    # 0을 만나면 택배 하차
    for i in range(start, end):
        temp[i] = amount
    # 0의 개수(하차 지점) 0번 인덱스에 저장
    temp[0] = (start, end)
    # 1-2. 2차원 배열에 저장[내리는 지점, 물건 이동 ...]
    arr.append(temp)

from pprint import pprint
# 시작지점 => 도착지점으로 정렬
arr.sort(key=lambda x: (x[0][0], x[0][1]))

# 2. 현재 지점에서 최대적재량만큼 택배 적재
stuff, iter =0, 1
current = [0 for _ in range(M)]
weight = 0
# 최종 output
result = 0
while stuff <= M and iter <= N:
    # 3. 택배를 내리게 되면 결과값에 가산
    for y in range(M):
        if not arr[y][iter] and current[y]:
            result += current[y]
            weight -= current[y]
            current[y] = 0
    if stuff == M:
        stuff += 1
        continue
    # 2-1. 현재 적재량과 비교해서 더 실을 수 있는지 판단
    if weight <= C:
        for i in range(stuff, M):
            if arr[i][iter] + weight <= C:
                # 무게 갱신해주고, 현재 택배 수하 리스트에 넣기
                weight += arr[i][iter]
                current[i] = arr[i][iter]
                stuff = i + 1
                if i == M - 1:
                    iter += 1
            # 최대 용량은 아니여서 일부는 가져갈 수 있을 때
            elif arr[i][iter]:
                current[i] = C - weight
                weight = C
                iter += 1
                stuff = i + 1
                break
            else:
                iter += 1
                stuff = i + 1
                break

    else:
        iter += 1

print(result)