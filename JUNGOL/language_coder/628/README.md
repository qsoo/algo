## 628. 파일입출력 - 자가진단3

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=265&sca=10i0)

1회독: 21.07.02



### my solution

```python
arr = []
for i in range(10):
    a, b = input().split()
    b = int(b)
    arr.append([i, a,b])

# 1. 정렬된 배열 생성
new_arr = sorted(arr, key=lambda x: x[2])

# 2. 나보다 큰 값의 개수를 구하면 내 등수 알 수 있음
for i in range(len(new_arr)):
    # 나보다 큰 값이 없으면 1등이니 초기 변수는 1
    temp = 1
    for j in range(i+1, len(new_arr)):
        if new_arr[i][2] < new_arr[j][2]:
            temp += 1
    # 2-1. 확인이 끝나면 등수 정보 리스트에 추가
    new_arr[i].append(temp)

# 3. 번호순 정렬
result = sorted(new_arr, key=lambda x: x[0])

# 4. 출력 형식에 맞게 출력
print('Name Score Rank')
for i in range(len(result)):
    print(f'{result[i][1]:>4} {result[i][2]:>5} {result[i][3]:>4}')
```

나보다 점수가 높은 사람 + 1이 내 현재 등수인 점을 이용해서 해결



### (틀린 코드)

```python
arr = []
for i in range(10):
    a, b = input().split()
    b = int(b)
    arr.append([i, a,b])

# 1. 정렬된 배열 생성
new_arr = sorted(arr, key=lambda x: -x[2])

# 2. 등수 추가
for i in range(len(new_arr)):
    new_arr[i].append(i+1)

# 3. 번호순 정렬
result = sorted(new_arr, key=lambda x: x[0])

# 4. 출력 형식에 맞게 출력
print('Name Score Rank')
for i in range(len(result)):
    print(f'{result[i][1]:>4} {result[i][2]:>5} {result[i][3]:>4}')
```

동점자를 처리하지 못하고 등수별 한 명씩만 넣는 코드

=> 동점자 처리 코드 추가



### 태그

- 정렬
- 문자열 포맷팅

