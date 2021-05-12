## 1411. 비슷한 단어

[문제링크](https://www.acmicpc.net/problem/1411)

1회독: 21.01.18



### Idea

전체적으로 문제 이해가 어려웠던 문제 

패턴이 같다, 소문자만 나온다 등이 Hint 

(1) aabc == zzcd ⇒ 이를 숫자로 바꿔서 생각하면 둘다 '1123'의 형태를 띄게 된다 

(2) index 메서드를 사용해도 되는 이유는 어차피 중복이 없기 때문에(중복도 1개만 추가) 이를 사용하여도 무방 

(3) 마지막 쌍 조회를 위해 100개 중 2개를 뽑는 조합의 개수이기 때문에 for문 두개를 이용해서 해결 가능 



### my solution 1

```python
# N: 총 단어의 개수
N = int(input())
arr = list(input() for _ in range(N))
# 비교를 위해 변환한 단어 담을 리스트
pair_li = []

for i in range(N):  # 100
    # 해당 단어에서 나오는 음절 저장 리스트
    temp = {}
    feature = 1
    number = 0
    for j in range(len(arr[i])):    # 50
        target = arr[i][j]

        if target in temp.keys():
            number = number * 10 + temp[target]

        else:
            temp[target] = feature
            number = number * 10 + temp[target]
            feature += 1

    # 2. 이를 비교 리스트에 저장
    pair_li.append(number)

# print(pair_li)

# 3. 같은 쌍이 몇개 있는지 확인
result = 0
# comb(100, 2) = 약 9900/2
for i in range(N-1):
    for j in range(i+1, N):
        if pair_li[i] == pair_li[j]:
            result += 1

print(result)
```



### my solution 2

```python
# N: 총 단어의 개수
N = int(input())
arr = list(input() for _ in range(N))
# 비교를 위해 변환한 단어 담을 리스트
pair_li = []

for i in range(N):  # 100
    # 해당 단어에서 나오는 음절 저장 리스트
    temp = []
    feature = 1
    number = 0
    for j in range(len(arr[i])):    # 50
        target = arr[i][j]

        if target in temp:
            number = number * 10 + temp.index(target)

        else:
            temp.append(target)
            feature += 1
            number = number * 10 + feature

    # 2. 이를 비교 리스트에 저장
    pair_li.append(number)

# print(pair_li)

# 3. 같은 쌍이 몇개 있는지 확인
result = 0
# comb(100, 2) = 약 9900/2
for i in range(N-1):
    for j in range(i+1, N):
        if pair_li[i] == pair_li[j]:
            result += 1

print(result)
```



### (틀린 코드)

```python
# N: 총 단어의 개수
N = int(input())
arr = list(input() for _ in range(N))
# 비교를 위해 변환한 단어 담을 리스트
pair_li = []

for i in range(N):
    # 해당 단어에서 나오는 음절 저장 리스트
    temp = []
    feature = 1
    number = 0
    for j in range(len(arr[i])):
        target = arr[i][j]

        if target in temp:
						# 이 부분에서 feature 정보를 갱신하게 되면 다음 음절 들어올 때 반영이 되서 틀림
            feature = temp.index(target)
            number = number * 10 + feature

        else:
            temp.append(target)
            # 1. 위에서 구한 특성을 숫자로 변환
            feature += 1
            number = number * 10 + feature


    # 2. 이를 비교 리스트에 저장
    pair_li.append(number)


# 3. 같은 쌍이 몇개 있는지 확인
result = 0
for i in range(N-1):
    for j in range(i+1, N):
        if pair_li[i] == pair_li[j]:
            result += 1

print(result)
```

위에서 temp안에 음절이 존재하면 feature을 변경해주는 것이 아니라 

그 값만 넣어주고 넘어가야 다음부터 진행할 때 오류가 생기지 않는다 

example)  

temp = ['a', 'b'] (문제의 if문을 진행하면) feature가 다시 0으로 갱신되므로 

이를 갱신시키지 않고 number만 변경 시켜줘야 한다!



### 태그

- 탐욕 알고리즘

