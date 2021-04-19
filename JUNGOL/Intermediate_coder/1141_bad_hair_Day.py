"""
# 시간초과
# N: 소들의 수
N = int(input().strip())
# 소들의 배열
arr = [int(input().strip()) for i in range(N)]

# 최종 결과값
result = 0

for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            result += 1
        else:
            break

print(result)
# 시간초과
# pivot 설정해서 반복
def count(arr: list):
    global result

    # 종료조건
    if len(arr) < 2:
        return

    else:
        # 1. max 값 찾기
        target = arr.index(max(arr))

        result += len(arr) - (target + 1)
        # left
        count(arr[:target])
        # right
        count(arr[target+1:])

# N: 소들의 수
N = int(input().strip())
# 소들의 배열
arr = [int(input().strip()) for i in range(N)]

# 최종 결과값
result = 0

count(arr)
print(result)

# 시간초과
# N: 소들의 수
N = int(input().strip())

# 소들의 배열
arr = []
# 결과값 저장
result = 0
for i in range(N):
    # 현재 들어오는 소
    cow = int(input().strip())

    # 비어있으면 바로 넣는다
    if not arr:
        arr.append(cow)
    # 비어 있지 않으면 현재 들어오는 것보다는 작은 애들은 다 없앤다
    else:
        temp = []
        for j in range(len(arr)):
            if arr[j] > cow:
                temp.append(arr[j])
                result += 1

        temp.append(cow)
        arr = temp

print(result)

# N: 소들의 수
import sys
N = int(sys.stdin.readline().strip())

# 소들의 배열
arr = []
# 결과값 저장
result = 0
for _ in range(N):
    # 현재 들어오는 소
    cow = int(sys.stdin.readline().strip())

    # 비어있으면 바로 넣는다
    if not arr:
        arr.append(cow)
    # 비어 있지 않으면 현재 들어오는 것보다는 작은 애들은 다 없앤다
    else:
        i = 0
        while i < len(arr):
            if arr[i] <= cow:
                arr.pop(i)
            else:
                i += 1
                result +=1

        arr.append(cow)

print(result)
"""
N = int(input())
cowList = []
for i in range(N):
    cowList.append(int(input()))

cowInput = []
result = 0

for i in range(N):
    firstTaller = -1

    travelDirection = True if len(cowInput) < 3 or abs(cowInput[0] - cowList[i]) < abs(cowInput[-1] - cowList[i]) else False
    travelNum = []

    if travelDirection:
        travelNum = range(len(cowInput))
    else:
        travelNum = range(len(cowInput) - 1, -1, -1)

    for j in travelNum:
        if cowInput[j] <= cowList[i]:
            firstTaller = j
            break

    if firstTaller != -1:
        result += firstTaller
        cowInput = cowInput[:firstTaller]
    else:
        result += len(cowInput)

    cowInput.append(cowList[i])

print(result)
