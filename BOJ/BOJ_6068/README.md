## 6068. 시간 관리하기

[문제 링크](https://www.acmicpc.net/problem/6068)

1회독: 21.01.29



### Idea

(1) 전체 가지고 있는 시간(S의 범위)으로 배열을 만들고  

(2) 일에 소요되는 시간을 index로 보고 해당 시간에 수행해야 하는 일이 있으면 앞으로 이동 

(3) 이런 식으로 주어진 업무를 배치를 시키고 최종적으로 index가 0보다 작게 되면 -1 

(4) 아니라면 value == 1의 바로 이전의 value가 0인 index가 일어나도 되는 시간 



### my solution

```python
# 1. 인덱스 - 시간, value 걸리는 시간 체크
arr = [0 for _ in range(10000001)]

# 2.n - 수행할 일의 개수 a - 걸리는 시간, b - 끝나는 시간
n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    # idx의 val 판별을 위한 변수
    i = 0
    is_can = False
    while i < a:
        # idx 범위 벗어나게 되면 주어진 업무 수행 불가
        if b - i < 0:
            is_can = True
            break
        # 해당 시간에 주어진 업무가 없을 때 => 바로 넣어주기
        if not arr[b - i]:
            arr[b - i] = 1
            i += 1

        # 해당 시간에 주어진 업무가 있을 때 => 주어진 업무 전에 빈 시간까지 이동
        else:
            b -= 1

    if is_can:
        break

# 가능한 시간 구하기
if is_can:
    print(-1)
else:
    print(arr.index(1) - 1)
```



