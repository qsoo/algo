# 1215. 회문 1

[문제링크](https://zzu.li/cq3tf)

1회독: 20.11.20



### idea

행과 열일 때의 케이스를 분리하여 생각 ⇒ 처음에는 행과 열에서 찾고자하는 회문의 길이만큼 뺀 부분을 탐색시키는 식으로 구현했지만 

다시 살펴보니 그렇게 되면 `[y][x]` index 기준으로 끝 x좌표에 있는 열 회문등이 탐색되지 않는 경우 발생 

따라서 케이스 분리 

2. 그 후 회문의 가운데 인덱스를 기준으로 왼쪽 끝과 오른쪽 끝이 같은지 비교



- my solution

```python
import sys
sys.stdin = open('1215.txt', 'r')

def check_palindrome_col(y, x):
    global result

    col_palindrome = ''
    for i in range(y, y + target):
        col_palindrome += arr[i][x]

    endpoint = target // 2

    # col 검사
    i = 0
    while i < endpoint:
        # idea - 왼쪽 끝과 오른쪽 끝을 비교한다
        if col_palindrome[i] == col_palindrome[-(i + 1)]:
            is_palindrome_col = True
        else:
            is_palindrome_col = False
            break
        i += 1

    if is_palindrome_col:

        result += 1


def check_palindrome_row(y, x):

    global result
    # 가로, 세로 탐색
    row_palindrome = arr[y][x:x+target]

    # 회문여부 검사하는 문장의 가운데에 오게 되면 종료
    endpoint = target // 2

    i = 0
    while i < endpoint:
        # row 검사
        if row_palindrome[i] == row_palindrome[-(i + 1)]:
            is_palindrome_row = True
        else:
            is_palindrome_row = False
            break
        i += 1

    if is_palindrome_row:

        result += 1


for tc in range(1, 11):
    # target: 찾아야하는 회문의 길이
    target = int(input())
    arr = [input() for _ in range(8)]

    # 2. 가져온 배열이 회문인지 판별
    # 3. 세로에서도 반복

    result = 0
    # 1. 타겟의 길이만큼 배열에서 가져오기 - 행, 열 나눠서
    for y in range(8):
        for x in range(8 - target + 1):
            check_palindrome_row(y, x)

    for y in range(8 - target + 1):
        for x in range(8):
            check_palindrome_col(y, x)

    print('#{} {}'.format(tc, result))
```



- 틀린 코드

```python
import sys
sys.stdin = open('1215.txt', 'r')


def check_palindrome(y, x):

    global result
    # 가로, 세로 탐색
    row_palindrome = arr[y][x:x+target]
    col_palindrome = ''
    for i in range(y, y+target):
        col_palindrome += arr[i][x]
    # 회문여부 검사하는 문장의 가운데에 오게 되면 종료
    endpoint = target // 2
    print(row_palindrome)
    print(col_palindrome)
    i = 0
    # col 검사
    while i < endpoint:
        # idea - 왼쪽 끝과 오른쪽 끝을 비교한다
        if col_palindrome[i] == col_palindrome[-(i + 1)]:
            is_palindrome_col = True
        else:
            is_palindrome_col = False
            break
        i += 1

    i = 0
    while i < endpoint:
        # row 검사
        if row_palindrome[i] == row_palindrome[-(i + 1)]:
            is_palindrome_row = True
        else:
            is_palindrome_row = False
            break
        i += 1
    if x == 5 and y == 1:
        print('여기')
        print(col_palindrome)
        print(is_palindrome_col)
    if is_palindrome_col:

        print('세로', col_palindrome)
        print()
        result += 1
    if is_palindrome_row:
        print('가로', row_palindrome)
        print()
        result += 1



for tc in range(1, 11):
    # target: 찾아야하는 회문의 길이
    target = int(input())
    arr = [input() for _ in range(8)]

    # 2. 가져온 배열이 회문인지 판별
    # 3. 세로에서도 반복

    result = 0
    # 1. 타겟의 길이만큼 배열에서 가져오기
    for y in range(8-target + 1):
        for x in range(8 - target + 1):
            check_palindrome(y, x)

    print(tc, result)
```

```
최대한 시간 단축에 집중하다보니 탐색하는 범위부터 잘못설정하는 실수 발생 => 행의 끝(x)에서 col들이 회문일 수도 있다! => 행, 열 탐색을 분기해서 생각
```



`2차원배열`



