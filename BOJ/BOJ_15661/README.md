## 15661. 링크와 스타트

[문제 링크](https://www.acmicpc.net/problem/15661)

1회독: 21.01.25



### Idea

멱집합(모든 부분집합들의 집합)을 구해서 차이를 구하면 되는 문제 전체 로직은 

(1) 팀을 만들 수 있는 모든 경우의 수로 배열 생성(A, B팀 분배) 

(2) 해당 팀일 경우의 시너지의 합을 구한뒤 절대값으로 차이를 구해줌 

(3) 최소값의 경우를 찾아서 이를 출력 시간초과 문제로 인해 pypi로 해결했다



### my solution 1

```python
# 20 * 20 * 2 * 20 * 20
def check_senergy(a:list, b:list):
    score_a, score_b = 0, 0

    # a팀의 총 점수 구하기
    if len(a) == 1:
        score_a = 0
    else:
        for i in range(len(a)-1):
            mate_1 = a[i]
            for j in range(i+1, len(a)):
                mate_2 = a[j]
                score_a += score[mate_1][mate_2] + score[mate_2][mate_1]

    # b팀의 총 점수 구하기
    if len(b) == 1:
        score_b = 0
    else:
        for i in range(len(b)-1):
            mate_1 = b[i]
            for j in range(i+1, len(b)):
                mate_2 = b[j]
                score_b += score[mate_1][mate_2] + score[mate_2][mate_1]

    # 최종 차이값 저장
    global result

    result = min(abs(score_a - score_b), result)
    return


def powerset(n:int, k:int):

    if n == k:
        temp_a = []
        temp_b = []
        for i in range(k):
            if visited[i] == 1:
                temp_a.append(i)
            else:
                temp_b.append(i)
        # 한 팀에 한 명이상이 있어야 한다
        if temp_a and temp_b and (temp_b, temp_a) not in all:
            check_senergy(temp_a, temp_b)
        return

    else:
				# 포함했을 때의 경우의 부분집합 구하는 부분
        visited[n] = 1
        powerset(n+1, k)
				# 포함하지 않았을 때의 부분집합을 구하는 부분
        visited[n] = 0
        powerset(n+1, k)


# 1. N: 인원수, score: 시너지를 내는 점수
N = int(input())
# 20
score = [list(map(int, input().split())) for _ in range(N)]
# 방문여부 check 20
visited = [0 for _ in range(N)]
all = []

result = float('inf')

powerset(1, N)
print(result)
```



### (틀린코드)

```python
# 1. N: 인원수, score: 시너지를 내는 점수
N = int(input())
# 20
score = [list(map(int, input().split())) for _ in range(N)]
# 방문여부 check 20
visited = [0 for _ in range(N)]

result = float('inf')
# 20 * 20 * 2 * 20 * 20
def check_senergy(a:list, b:list):
    score_a, score_b = 0, 0

    # a팀의 총 점수 구하기
    if len(a) == 1:
        score_a = 0
    else:
        for i in range(len(a)-1):
            mate_1 = a[i]
            for j in range(i+1, len(a)):
                mate_2 = a[j]
                score_a += score[mate_1][mate_2] + score[mate_2][mate_1]

    # b팀의 총 점수 구하기
    if len(b) == 1:
        score_b = 0
    else:
        for i in range(len(b)-1):
            mate_1 = b[i]
            for j in range(i+1, len(b)):
                mate_2 = b[j]
                score_b += score[mate_1][mate_2] + score[mate_2][mate_1]

    return abs(score_a - score_b)

def powerset(n:int, k:int):
    # 최종 차이값 저장
    global result
    
    if n == k:
        temp_a = []
        temp_b = []
        for i in range(k):
            if visited[i] == 1:
                temp_a.append(i)
            else:
                temp_b.append(i)
        # 한 팀에 한 명이상이 있어야 한다
        if temp_a and temp_b:
            result = min(result, check_senergy(temp_a, temp_b))
        return

    else:
				# 포함했을 때의 경우의 부분집합 구하는 부분
        visited[n] = 1
        powerset(n+1, k)
				# 포함하지 않았을 때의 부분집합을 구하는 부분
        visited[n] = 0
        powerset(n+1, k)

powerset(0, N)
print(result)
```

완전탐색으로 접근하여 

(1) 팀을 만들 수 있는 모든 경우의 수로 배열 생성(A, B팀 분배) 

(2) 해당 팀일 경우의 시너지의 합을 구한뒤 절대값으로 차이를 구해줌 

(3) 최소값의 경우를 찾아서 이를 출력 하는 식으로 접근했지만 시간초과 발생



### 태그

- 탐욕 알고리즘

