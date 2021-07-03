## 2605. 줄 세우기

[문제 링크](https://www.acmicpc.net/problem/2605)

1회독: 20.08.27



### my solution

```python
T = int(input())  # 학생 수
students = list(map(int, input().split()))  # 학생들 뽑은 수

# 학생들 번호 리스트 생성
num_students = [i for i in range(1, len(students)+1)]

result = [] # 최종 배열

# 뽑은 수 리스트에 접근해서 insert로 삽입시키기
for idx, student in enumerate(students):
    # 이동한만큼 나머지 뒤로 밀기
    result.insert(len(result) - student, num_students[idx])

for i in result:
    print(i, end=' ')
```

1.  built-in 함수인 insert를 사용하여 뒤로 미는 부분 간소화 구현
   	*list.insert(index, value) : list의 index위치에 value 값을 넣겠다
2. for문을 통한 출력으로 출력형식 맞춰줌



### (틀린 코드)

```python
# 학생들 번호 리스트 생성
num_students = [i for i in range(1, len(students)+1)]

# 1, 2 => 1, 2, 3 ... 이런 식으로 num_students 요소에 접근
for idx in range(len(num_students)):
    if students[idx] == 0:
        result[idx] = num_students[idx]

    # 0이 아니면 0보다 크다
    elif students[idx] != 0:
        # 앞으로 이동한만큼 원래 있던 값들 뒤로 밀어줘야함
        for i in range(students[idx]):
            result[idx] = result[idx - (students[idx])]
            result[idx - (students[idx])] = num_students[idx]

    print(result)
```

해당 방법은 이동이 1인 경우에만 작동함
즉, 앞으로 간만큼 나머지 요소들을 뒤로 밀어야 하는데 이 부분이 구현이 어려웠음



### 태그

- 리스트

