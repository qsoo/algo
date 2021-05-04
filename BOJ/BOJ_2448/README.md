## 2448. 별찍기 - 11

- 재귀



### Idea

프랙탈 꼴로 그려진 별표를 프린트하는 문제 

전체적으로 규칙을 찾는데는 많은 시간이 걸리지 않았지만 

규칙을 적용하는데 어떤 식으로 적용해야하는지 몰라서 헤맸던 문제 

결국에는 혼자 힘으로 풀지 못하고 다른 사람들의 풀이를 보고 풀었는데도 어떤 식으로 작동하는지 한참을 공부해서 푼 문제로 다시 한번 풀어봐야할 것 같다. 

핵심은  

(1) 삼각형이 계속 생길 때 공백 추가를 어떤 식으로 할지 

(2) 어떤 부분으로 나눠서 생각할지(삼각형 1개와 2개 꼴로 이뤄짐)



```python
import math
# 1. 새롭게 추가될 삼각형 자리를 만들어 준다 - 이 전의 삼각형의 두개가 생긴다
def add_new_triangle_pair():
    for i in range(len(triangle)):
        # 밑으로 왼쪽, 오른쪽 양쪽에 생긴다
        triangle.append(triangle[i] * 2)

# 2. 새로운 삼각형이 만들어지면 변형시키기(띄어쓰기)
def push_to_right(k:int):
    # 1. 전체 중에서 위에 배치된 삼각형만 밀면된다(상단)
    for i in range(len(triangle) // 2):
        triangle[i] = ' '*(3*(2**k)) + triangle[i] + ' '*(3*(2**k))

# 별표 찍기에 사용할 예시
triangle = ['  *   ', ' * *  ', '***** ']
N = int(input())
# N == 3 * (2 ** k) 꼴
K = int(math.log(N // 3, 2))

if N != 3:
    for k in range(K):
        add_new_triangle_pair()
        push_to_right(k)

for x in triangle:
    print(x)
```

