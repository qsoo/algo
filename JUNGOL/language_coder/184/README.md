## 184. 문자열1 - 형성평가3

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=84&sca=10e0)

1회독: 21.06.11



### my solution 1

```python
# ASCII
# 32 ~ 64 특수문자
# 48 ~ 57 숫자
# 91 ~ 96 특수문자
# 122(z)

for i in input():
    temp = ord(i)
    # 알파벳, 숫자만
    if 48 <= temp <= 122:
        # 대문자이면 소문자로
        if 65 <= temp <= 90:
            print(i.lower(), end='')
        # 숫자, 소문자 그대로 출력
        elif 48 <= temp <= 57 or 97 <= temp <= 122:
            print(i, end='')
```

ASCII 코드를 이용해서 조건문 분기

### my solution 2

```python
# 정규식 사용
import re
# 숫자 + 문자: '/w'에서 '_' 제외
num = re.compile('[a-zA-Z0-9]')

# findall
result = num.findall(input())
print("".join(x.lower() for x in result))
```

정규식을 이용 

(1) findall로 일치하는 모든 값 추출 후 

(2) 알파벳은 소문자로 변경하고 

(3) join으로 형태에 맞게 출력



### 참고 자료

- `.upper()`: 모든 알파벳을 대문자로 변환
- `.capitalize()` : 주어진 문자열의 맨 첫 글자를 대문자로 변환
- `.title()` : 주어진 문자열에서 알파벳 외의 문자(숫자, 특수기호, 띄어쓰기 등)로 나누어져 있는 알파벳 단어들의 첫 글자를 대문자로 변환
- `.lower()` : 모든 알파벳을 소문자로 변환



### 태그

- 문자열
- ASCII
- 정규식