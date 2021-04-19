'''
# 1. recursive

# 1. N: 정수의 개수, S: 합
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 방문여부 체크
visited = [0 for i in range(N)]
cnt = 0

def powerset(k:int=0, total:int=0):
    global cnt

    # 2. 종료조건 모든 부분집합 다 찾았다
    if k == N:
        # 1. 첫 종료조건 total == S and 공집합 X일 때
        if total == S and sum(visited):
            cnt += 1
        return
    else:
        visited[k] = 1
        total += arr[k]
        powerset(k+1, total)
        visited[k] = 0
        total -= arr[k]
        powerset(k+1, total)

powerset()
print(cnt)

# 2. bit masking
# 1. N: 정수의 개수, S: 합
N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for i in range(1 << N):
    total = 0
    for j in range(N):
        if i & (1 << j):
            total += arr[j]
    if i and total == S:
        cnt += 1

print(cnt)

'''
nums = [-7, -3, -2, 5, 8]
T=[0]
for n in nums:
    A=T[:]
    for a in A:
        T.append(a+n)
c=T[1:].count(S)
print(c)