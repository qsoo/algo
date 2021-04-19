# 1. 재귀로 구현
def binary_search(start:int, end:int, target:int=0):
    # 0. 종료 조건은 start > end일 때:
    cnt = 0
    mid = (start + end) // 2
    target = mid
    if start > end:
        return target

    for i in range(len(arr)):
        cnt += arr[i] // mid

    # 조건을 만족하면 더 큰 값 찾기
    if cnt >= N:
        start = mid + 1
    # 조건을 만족하지 못하면 더 작은 값 찾기
    else:
        end = mid - 1

    return binary_search(start, end, target)

# K: 이미 가지고 있는 랜선의 개수, N: 만들어야되는 랜선의 개수
K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
print(binary_search(1, max(arr)))

# 2. while문 이용
# start를 0으로 지정하면 zerodivisionError 발생 가능 : start, end = 0, 1 일 때
start, end = 1, max(arr)
# 찾고자하는 길이의 값
target = 0
# 오른쪽 가르키는 인덱스가 왼쪽보다 작아지면 검색 종료
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for line in arr:
        cnt += line // mid

    # mid < target 우측 탐색 실시 == start <- mid + 1
    if cnt >= N:
        start = mid + 1
        target = mid
    # mid > target 좌측 탐색 실시 == end <- mid - 1
    else:
        end = mid - 1

print(target)
