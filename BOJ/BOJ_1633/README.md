## 1633. 최고의 팀 만들기

[문제링크](https://www.acmicpc.net/problem/1633)

1회독: 21.01.12



### my solution - DP

```python
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
```

모든 경우의 수를 기록할 DP라는 배열을 만들어서

해당 단계가 지나가면서 가장 큰 값들이 남아서 다음 단계로 진행하기 때문에 

최종적으로 가장 큰 값을 구할 수 있게 된다.

단, 이 방법은 몇 번째의 참가자를 선택하였고 black, white로 배치하였는지는 알 수 없다 

(1) 전체 총 경우의 수에서 1번 참가자 - 포함 X / black / white 로 쭉 진행하여



### (틀린 코드)

```python
import sys

# 입력 받기 (white, black)
arr = []
for line in sys.stdin:
    if line == '\n':
        break
    line = tuple(map(int, line.split()))
    arr.append(line)

result = [0, 0]
val = 0

for i in range(2):
    temp = 0
    # white -> black 순으로 가장 큰 값들 가져오기 / black -> white 순으로 가장 큰 값들 가져오기
    result[i] = sorted(arr, key=lambda x: x[i], reverse=True)
    for j in range(15):
        temp += result[i][j][0]
    result[i] = result[i][15:]

    result[i] = sorted(result[i], key=lambda x: x[1-i], reverse=True)
    for j in range(15):
        temp += result[i][j][1]

    if temp > val:
        val = temp

print(val)
```

흑 - 백 or 백 - 흑 순서로 내림차순 정렬을 해서 상위 값을 가져오면 되지 않을까라고 생각했으나 

이는 예시 케이스에서도 맞지 않고 

많은 입력을 받게 되면 맞지 않는 edge case가 많이 나올 것으로 추정된다