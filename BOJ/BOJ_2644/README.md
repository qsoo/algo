## 2644. 촌수계산

[문제 링크](https://www.acmicpc.net/problem/2644)

1회독: 20.08.28



### (틀린 코드)

my solution 1

```python
def check(sp):

    # end point 방문했는지 확인
    while sp != ep:

        # start point visit
        visited[sp] = 1

        # 촌수 계산을 위해 route를 넣어줄 리스트 생성
        if not sp in result:
            result.append(sp)

        # 인접 행렬 중 방문 안 한 노드 찾기
        for i in adjacent_matrice[sp]:

                if not visited[i]:
                    visited[i] = 1
                    sp = i
                    break
        # pop
        else:
            result.pop()
            check(sp)

    return len(result)

N = int(input())    # 전체 사람 수(node)
sp, ep = map(int, input().split())  # 촌수 계산 대상
M = int(input())    # 부모 - 자식 관계의 수 (edge)

# 인접행렬 만들기
adjacent_matrice = [[] for _ in range(N + 1)]

for m in range(M):
    parent, child = map(int, input().split())
    adjacent_matrice[parent].append(child)
    adjacent_matrice[child].append(parent)

visited = [0] * N
# route
result = []
# 촌수 체크
count = check(sp)
print(count)
```

DFS로 구현을 해보려고 했는데 예제 데이터에서는 작동하는데 문제 제출하면 런타임 에러가 난다. 

뭔가 처리 부분이 미진한 것 같은데 이 부분은 주말 문제랑 함께 일요일에 차분히 해결해보자!



my solution 2

```python
def check(sp):
    # 초기 조건 설정
    visited[sp] = 1

    if not sp in result:
        result.append(sp)

    # end point 방문했는지 확인
    while sp != ep and result:

        # start point visit
        visited[sp] = 1

        # 인접 행렬 중 방문 안 한 노드 찾기
        for i in adjacent_matrice[sp]:

                if not visited[i]:
                    visited[i] = 1
                    sp = i
                    break

        # 촌수 계산을 위해 route를 넣어줄 리스트 생성
        if not sp in result:
            result.append(sp)
        # pop
        else:
            result.pop()
            # 위에서 노드를 찾을 때 sp의 값이 바뀌므로 재귀함수를 호출하면 계속 돌게됨
            sp = result[-1]
    if result:
        return len(result)

    else:
        return -1
```

촌수가 없는 경우의 처리가 안됨

 

### 태그

- 그래프
- BFS
- DFS

