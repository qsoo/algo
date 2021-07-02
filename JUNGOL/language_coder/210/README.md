## 210. 파일입출력 - 형성평가6

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=110&sca=10i0)

1회독: 21.07.02



### my solution

```python
def upper(n:int):
    for i in range(n):
        print(f'{"* " * (2 * i + 1):^{4*n - 2}}')


def lower(n:int):
    for i in range(n - 1, 0, -1):
        print(f'{"* " * (2 * i - 1):^{4*n - 2}}')


def result(n:int):
    upper(n)
    lower(n)

result(int(input().strip()))
```

주어진 출력의 모양을 보면 중간을 기준으로 위, 아래가 대칭인 것을 확인할 수 있다

(1) 위의 별표 모양을 찍는 함수를 만든다(여기서 가장 길이가 긴 길이 포함)

(2) 나머지 아래 부분을 만든다

(3) 두 함수를 실행시키는 함수를 만든다

추가적으로 문자열 포매팅 형식을 이용해서 차지하는 칸의 개수 지정



### 태그

- 문자열 포맷팅
- 함수