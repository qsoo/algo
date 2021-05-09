## 14501. 퇴사

[문제링크](https://www.acmicpc.net/problem/14501)

1회독: 21.01.06



### my solution 1

DFS

```python
# 현재일자, 지금까지의 합
def dfs(day, total):
    # 종료조건 - 퇴사날 되었다
    if day >= N:
        global income
        if income < total:
            income = total
        return

    # 1. 현재시점 상담한다
    if day + arr[day][0] <= N:
        dfs(day + arr[day][0], total + arr[day][1])
    # 2. 상담안하고 다음으로 넘어간다
    if day + 1 <= N:
        dfs(day + 1, total)


# N: 일하는 일수 - index
N = int(input())
# (걸리는 일 수, 버는 금액)
arr = [tuple(map(int, input().split())) for _ in range(N)]

# 최대수익
income = 0
# 1. 시작지점을 탐색하면서 최대 금액 확인
dfs(0, 0)

print(income)
```

현재 시점을 기준으로 일을 했을 때와 안했을 때의 경우를 모두 구해서 최대값을 구하면 되는 문제

그 과정에서 현재 시점에서 일을 한다면 걸리는 시간만큼 인덱스를 뛰어넘어서 수입의 총합을 구하면 된다

### my solution 2

DP

```python
# 2. DP
# N: 일하는 일수 - index
n = int(input())
# (걸리는 일 수, 버는 금액)
arr = [tuple(map(int, input().split())) for _ in range(n)]
charge = list(map(lambda x: x[1], arr))

for i in range(n):
    # 할 수 없는 일이 들어오게되면 해당 부분은 버는 돈이 0이다
    if i + arr[i][0] > n:
        charge[i] = 0
        continue
    # 현재까지 벌 수 있는 가장 큰 수입으로 t를 만들어준다
    t = charge[i]
    # 여기까지 수행했을 때 할 수 있는 상담업무의 날짜를 계산해서 start지점으로
    for j in range(i + arr[i][0], n):
        # 해당지점에 저장되어 있는 수입보다 지금까지 계속 일을 했을 때 수입이 크면 큰 값으로
        if t + arr[j][1] > charge[j]:
            charge[j] = t + arr[j][1]
            
# 가장 큰 값을 골라서 출력
print(max(charge))
```

앞에서부터 일을 수행해나가면서 해당 지점에 수입보다 그 전까지의 일을 했던 수입이 크다면 이를 갱신해줘서 

결론적으로 수행할 수 있는 최종적인 가장 큰 수입을 얻는 방법



### 틀린코드

```python
# 0. 종료조건은 현재 최대벌이보다 남은 것들을 다 더해도 작을 때
# 1. 걸리는 기간에 접근해서 재귀로 돌린다 [st:ed] 넘겨준다 -for로 하나씩 넣으면서
# 2. 최대 벌이 출력


# present 현재까지의 수입 총합과 지금까지 비교할 리스트 부분 넘겨주기
def dfs(present:int, li:list):
    global income
    # 1. 가지치기 - 현재상태에서 현재의 최대수입보다 클 수 없을 때
    total = 0
    for i in range(len(li)):
        total += li[i][1]

    if present + total < income:
        return

    # 종료조건 - 더 이상 일할 수 없을 때


    # 2. 걸리는 기간 확인
    for i in range(len(li)):
        # 2-1. out of index
        day = li[i][0]
        temp = li[i][1]

        if i + day <= len(li) - 1:
            dfs(present + temp, li[i + day:])

        # 마지막을 포함할 경우
        elif i + day == len(li):
            if present + temp > income:
                income = present + temp

        elif i + day > len(li) - 1:
            if present > income:
                income = present
            return


# N: 일하는 일수 - index
N = int(input())
# (걸리는 일 수, 버는 금액)
arr = [tuple(map(int, input().split())) for _ in range(N)]

# 최대수익
income = 0
# 1. 시작지점을 탐색하면서 최대 금액 확인
for i in range(len(arr)):
    day = arr[i][0]
    dfs(arr[i][1], arr[i+day:])

print(income)
```

끼워 맞추기 식으로 설계를 해서 중간 중간 edge point가 다수 존재할 것으로 보인다.