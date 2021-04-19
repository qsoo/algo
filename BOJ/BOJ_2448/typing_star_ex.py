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