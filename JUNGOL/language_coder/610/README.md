## 610. 문자열2 - 자가진단9

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=247&sca=10f0)

1회독: 21.06.14



### my Idea

문자열 크기 역순으로 정렬한다는 말이 잘 이해되지 않아서 처음 접근을 잘못했던 문제 

문자열에서 모든 문자들의 아스키 코드 값을 합해서  

그 크기의 역순으로 배치하는 것이 아니라 

'abc', 'cde' 가 있으면 

(1) 'a'와 'c'의 아스키 코드 값을 비교 ( 97 < 99) 

(2) 'cde', 'abc' 순으로 배치해서 출력



### my solution

```python
# 1. 5개 문자 입력받기
arr = []
for _ in range(5):
    arr.append(input().strip())
# arr = list(input().strip()) # 이런 식으로 쓰면 문자 하나씩 원소로 들어감['J','u' ...]

# 2. 문자열 역순 정렬(아마도 앞부터 순서 비교해서 숫자가 큰 값이 맨 앞으로 나오는 식)
for i in range(4):
    for j in range(0, 4 - i):
        # 3. 각 문자열의 수 구하기
        for k in range(len(arr[j])):
            if ord(arr[j][k]) < ord(arr[j + 1][k]):
                # 4. swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                break
            elif ord(arr[j][k]) > ord(arr[j + 1][k]):
                break

print('\n'.join(string for string in arr))
```

거품 정렬의 방식을 응용해서 (1) 아스키 코드 값이 크면 앞으로 가져오기 (2) 이를 맨 앞까지 반복



### 태그

- 문자열
- ASCII
- 거품 정렬