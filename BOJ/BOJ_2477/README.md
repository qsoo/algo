## 2477. 참외밭

[문제 링크](https://www.acmicpc.net/problem/2477)

1회독: 20.08.26



### my solution

```python
T = int(input())    # 1m^2에 자라는 참외의 개수

field = [int(input().split()[1]) for _ in range(6)]

# 가장 긴 변의 길이 추출
max_length_1= max(field)
idx1 = field.index(max_length_1)
# 양 옆의 인덱스에 접근해서 나머지 가장 긴 변 추출
if field[idx1 - 1] <= field[(idx1 + 1) % 6]:
    max_length_2 = field[(idx1 + 1) % 6]
    first = idx1
else:
    max_length_2 = field[idx1 - 1]
    first = idx1 - 1

# small Rectangle
small_1, small_2 = field[(first + 3) % 6], field[(first + 4) % 6]

print(((max_length_1 * max_length_2) - (small_1 * small_2)) * T)
```

input 받을 때 선택해서 필요한 것만 받을 수 있음

(1) simple is best라고 max로 간단하게 가장 긴 변 구해서 인덱스 접근으로 방법 선회

(2) 마지막 인덱스에 매달려서 시간을 많이 버렸는데 생각해보니 [0],[6]에 있는 케이스의 경우 

대소 비교로 접근하면 나중 인덱스가 [6]으로 잡혀서 여기에 계속 빠져서 오류가 발생 

=> 먼저 나오는 인덱스를 기준으로 변경

(3) 대소 비교시에도 % 6 꼭 사용하기



### (틀린 코드)

my solution 1

```python
T = int(input())    # 1m^2에 자라는 참외의 개수

# direction - idx : 0 / move - idx : 1 인 2차원 array 생성
direction_field = [list(map(int, input().split())) for _ in range(6)]
'''
idea : 가장 긴 변의 직사각형에서 참외밭이 아닌 부분의 넓이를 빼겠다
hint : 반시계방향, 육각형
가장 긴 변은 반시계방향으로 가면 인접 인덱스이고,
가장 긴 변의 다다음에 나오는 길이 2개가 작은 직사각형의 넓이 구할 수 있음
'''

N = len(direction_field)    # 변의 개수(6)
direction, move = [], []    # 따로 저장하겠다
for i in range(N):
    direction.append(direction_field[i][0])
    move.append(direction_field[i][1])

max_move1, max_move2 = [0]*2, [0]*2 # [idx, length] 형태로 저장

# 평행한 변들은 인덱스 홀수 / 짝수에 같이 있음을 이용 새 리스트 생성
for i in range(N):

    if i % 2 and max_move2[1] <= move[i]:
        max_move2[0] = i
        max_move2[1] = move[i]
    elif i % 2 == 0 and max_move1[1] <= move[i]:
        max_move1[0] = i
        max_move1[1] = move[i]

# 가장 바깥쪽의 길이 두 개중 뒤에 오는 인덱스 => 한 칸 뛰고 접근하면 빈 공간 구성하는 변들
if max_move2[0] < max_move1[0]:
    small_move1, small_move2 = move[max_move1[0] + 2], move[max_move1[0] + 3]
else:
    small_move1, small_move2 = move[max_move2[0] + 2], move[max_move2[0] + 3]

result = ((max_move1[1] * max_move2[1]) - (small_move1 * small_move2))* T

print(result)
```

생각해보니 해당 방법은 가장 긴 변들이 리스트에 뒤쪽에 있으면 list indexing error 발생



my solution 2

```python
# 가장 바깥쪽의 길이 두 개중 뒤에 오는 인덱스 => 한 칸 뛰고 접근하면 빈 공간 구성하는 변들
if max_move2[0] < max_move1[0]:
    small_move1, small_move2 = move[(max_move1[0] + 2) % 6], move[(max_move1[0] + 3) % 6]
else:
    small_move1, small_move2 = move[(max_move2[0] + 2) % 6], move[(max_move2[0] + 3) % 6]

result = ((max_move1[1] * max_move2[1]) - (small_move1 * small_move2))* T

print(result)
```

위와 나머지 부분은 동일하고 작은 사각형의 변을 찾는 방법을 달리함

OutOfIndex를 방지하기 위해 % 6 연산 사용

=> 0 .. 5 까지의 index 중 0, 1, 2의 경우 out이 안되지만

3 => (5, 6) / 실제 : (5, 0)

4 => (6, 7) / 실제 : (0, 1)

5 => (7, 8) / 실제 : (1, 2)

임을 이용

그런데 답이 틀렸다고 나옴 => 이유를 잘 모르겠음



my solution 3

```python
T = int(input())    # 1m^2에 자라는 참외의 개수

# direction / move 따로 저장
direction_field = [list(map(int, input().split())) for _ in range(6)]

'''
idea : 가장 긴 변의 직사각형에서 참외밭이 아닌 부분의 넓이를 빼겠다
hint : 반시계방향, 육각형
가장 긴 변은 반시계방향으로 가면 인접 인덱스이고,
가장 긴 변의 다다음에 나오는 길이 2개가 작은 직사각형의 넓이 구할 수 있음
'''

# 한번 나온 방향인 애들이 가장 큰 사각형의 변의 길이
four_side = [0] * 5 # 방향 나온 횟수 저장

N = len(direction_field)    # 변의 개수(6)
move = []   # 이동거리 리스트
for y in range(N):
    move.append(direction_field[y][1])
    four_side[direction_field[y][0]] += int(direction_field[y][0] / direction_field[y][0])

max_length = []# 가장 긴 변의 길이
for idx, val in enumerate(four_side):
    if val == 1:
        for y in range(N):
            if direction_field[y][0] == idx:
                max_length.append(direction_field[y][1])



idx_1= move.index(max_length[0])
idx_2= move.index(max_length[1])

small_length = [0] * 2

if idx_1 <= idx_2:  # 인덱스가 큰 것의 옆으로 2, 3칸
    small_length[0] = move[(idx_2 + 2) % 6]
    small_length[1] = move[(idx_2 + 3) % 6]
else:  # 인덱스가 큰 것의 옆으로 2, 3칸
    small_length[0] = move[(idx_1 + 2) % 6]
    small_length[1] = move[(idx_1 + 3) % 6]

print((max_length[0]*max_length[1] - small_length[0] * small_length[1]) * T)
```

방향을 기준으로 한번 나오면 가장 긴 변의 길이인 것을 이용



### 태그

- 표준입출력
- 인덱스