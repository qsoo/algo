## 2491. 수열

[문제 링크](https://www.acmicpc.net/problem/2491)

1회독: 20.08.25



### my solution

```python
N = int(input())    # 수열의 길이
sequence = list(map(int, input().split()))  # 수열 들어있는 list

max_bigger, max_smaller = 1, 1   # 수열의 길이
total = 1

# bigger
for idx in range(N - 1):    # out of index 막자
    # out of index가 아닌 것 and 3개 더한게 2개 더한거 보다 클 때
    if sequence[idx] <= sequence[idx + 1]:
        total += 1
    else:
        total = 1    # reset

    # 제일 큰 값만 저장
    if max_bigger <= total:
        max_bigger = total

# smaller
total = 1   # reset
for idx in range(N - 1):    # out of index 막자
    if sequence[idx] >= sequence[idx + 1]:
        total += 1

    else:
        total = 1

    # 제일 큰 값만 저장
    if max_smaller <= total:
        max_smaller = total


# 둘 중에 큰 값 가져오기
if max_bigger <= max_smaller:
    print(max_smaller)

else:
    print(max_bigger)
```

(1) 시간 초과였던 이중 순회 삭제

(2) for문 하나에 커지는 경우 / 작아지는 경우 한번에 넣고자 하였으나 그럴 경우 total의 초기화가 복잡해짐 

=> 두 개의 case로 나눠서 풀이

(3) 순열의 길이 주어지니까 len()함수를 사용해서 구하지 않고 범위 설정



### (틀린 코드)

```python
# N = int(input())    # 수열의 길이
# sequence = list(map(int, input().split()))  # 수열 들어있는 list

# 1. 커지는 경우
bigger, smaller = [0] * len(sequence), [0]*len(sequence)

length = 1  # 길이값 저장(나 하나 항상 존재)

for i in range(1, len(sequence)):
    # 초기화 조건
    idx = i
    length = 1
    while idx <= (len(sequence) - 1):
            # 1부터 순회를 시켜서 요소들 비교
            if sequence[idx-1] <= sequence[idx]:
                length += 1
                idx += 1
            # 조건 만족 못하면 그만세기
            else:
                # 해당 리스트 요소 자리에 넣어주기
                bigger[i-1] = length
                length = 1
                idx = i
                break

    # 2. 작아지는 경우
    while idx <= (len(sequence) - 1):
            # 1부터 순회를 시켜서 요소들 비교
            if sequence[idx-1] >= sequence[idx]:
                length += 1
                idx += 1
            # 조건 만족 못하면 그만세기
            else:
                # 해당 리스트 요소 자리에 넣어주기
                smaller[i-1] = length
                length = 1
                idx = i
                break

if max(smaller) > max(bigger):
    print(max(smaller))
else:
    print(max(bigger))
```

시간 초과

```python
iteration = 0
bigger_result, smaller_result = [], []

for i in range(len(sequence) - 2):
    # 0. slicing 이용
    sequence = sequence[i:]
    total_bigger, total_smaller = 1, 1   # 수열의 길이
    for idx in range(len(sequence) - 1):    # out of index 막자
        # out of index가 아닌 것 and 3개 더한게 2개 더한거 보다 클 때
        # bigger
        if sequence[idx] * 2 <= sequence[idx] + sequence[idx + 1]:
            total_bigger += 1
        else:
            bigger_result.append(total_bigger)
            total_bigger = 1    # reset

        # smaller
        if sequence[idx] * 2 >= sequence[idx] + sequence[idx + 1]:
            total_smaller += 1

        else:
            smaller_result.append(total_smaller)
            total_smaller = 1

# 둘 중에 큰 값 가져오기
print(max(smaller_result + bigger_result))
```

시간 초과



### 태그

- DP