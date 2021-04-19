# N: 기둥의 개수
N = int(input())
arr = []

# 1. 기둥 정보 넣기
for _ in range(N):
    l, h = map(int, input().split())
    arr.append((l, h))
# 1-1. 기둥위치에 따라 정렬
arr.sort(key=lambda x : x[0])
print(arr)

ware_house = [0 for _ in range(arr[-1][0] + 1)]

for i in range(N):
    ware_house[arr[i][0]] = arr[i][1]

print(ware_house)
for i in range(1, N):
    if ware_house[i]:
        ware_house = ware_house[i:]
        break

# 2. 현재 배열에서 max값 찾기
pivot = ware_house.index(max(ware_house))

def left_check(l, r):
    # break 조건
    if l >= r:
        return
    # 1. 왼쪽의 sub_max 값 찾기
    sub_p = ware_house[:r].index(max(ware_house[:r]))
    # 2. sub_p ~ r까지 값 갱신
    for i in range(sub_p, r):
        ware_house[i] = ware_house[sub_p]

    left_check(l, sub_p)

def right_check(l, r):
    # break 조건
    if l >= r:
        return
    # 1. 오른쪽의 sub_max 값 찾기
    sub_p = ware_house[l:].index(max(ware_house[l:])) + l
    # 2. sub_p ~ r까지 값 갱신
    for i in range(l, sub_p):
        ware_house[i] = ware_house[sub_p]

    right_check(sub_p+1, r)
def check(l, p, r):
    left_check(l, p)
    right_check(p+1, r)

    return sum(ware_house)


print(check(0, pivot, len(ware_house) - 1))