## 9095. 1, 2, 3 더하기

[문제링크](https://www.acmicpc.net/problem/9095)



### Idea

1, 2, 3을 이용해서 주어지는 수를 만드는 문제

(알아야할 사항) 순서와 관계있기 때문에( 1 + 2 와 2 + 1은 각각 다른 케이스다!) 

(1) 주어진 N을 만드는 중복을 허용하는 순열과 같다 

(2) N이 11이하로 주어지기 때문에 경우의 수가 많지 않다 *3^11 = 약 17만

BFS를 이용해서 순서가 있는 리스트를 만들어서 개수를 탐색하는 방법으로 해결하였다



*(추가적으로 다음에 풀 때는)*

*(이 전 시행까지의) 총합을 매개변수로 들고 함수가 진행되는 형태에서 어떻게 하면 불필요한 진행을 가지치기 할 수 있을지 생각해봐야 한다(이미 답을 넘어서면 더 더해도 넘어선다!) 현재는 continue를 통해 연산을 안하는 형태지만 전체 케이스 탐색은 다 하고 있다.*



```python
# 1. queue를 만들어서 리스트(1, 2, 3), 이전까지의 합 정보를 가져간다
# 2. N과 리스트의 합이 같아질 때 break

def one_two_three_plus(perm:list, total:int):
    global cnt
    # perm: 현재까지 저장된 배열, total: 현재까지 가지고 있는 합
    queue = []
    queue.append((perm, total))
    while queue:
        new_perm, new_total = queue.pop(0)
        # 1. 종료조건( == N)
        if new_total == N:
            cnt += 1
            continue
        # 2. 숫자가 초과할 때
        elif new_total > N:
            continue
        else:
            queue.append((new_perm + [3], new_total + 3))
            queue.append((new_perm + [2], new_total + 2))
            queue.append((new_perm + [1], new_total + 1))

    return

for tc in range(int(input())):
    N = int(input())
    result = []
    total = 0
    # 총 개수
    cnt = 0
    one_two_three_plus(result, total)
    print(cnt)
```



**태그**

- BFS
- 완전 탐색

