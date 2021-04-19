# sw expert academy

## 2027. 대각선 출력하기

주어진 텍스트를 그대로 출력하세요.

```
#++++
+#+++
++#++
+++#+
++++#
```

- solution

```python
for i in range(5):
    print( ('+' * i)+ '#' +('+' * (4 - i)) )
```



## 2029. 몫과 나머지 출력하기

2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

**[제약 사항]**

각 수는 1이상 10000이하의 정수이다.


**[입력]**

가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.

각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.


**[출력]**

출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 몫을 출력하고 공백을 한 칸 둔 다음 나머지를 출력한다.

(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

- 입력

```
3   
9 2  
15 6 
369 15
```

- 출력

```
#1 4 1
#2 2 3
#3 24 9
```

- solution

```python
# 처음 input은 테스트 케이스의 수 : T
T = int(input())
# 다음부터 a와 b를 받아와서 a // b & a % b 출력
for i in range(T):

    a, b = map(int, input().split())
    
    print(f'#{i+1} {a // b} {a % b}')
```



## 2043. 서랍의 비밀번호

서랍의 비밀번호가 생각이 나지 않는다.

비밀번호 P는 000부터 999까지 번호 중의 하나이다.

주어지는 번호 K부터 1씩 증가하며 비밀번호를 확인해 볼 생각이다.

예를 들어 비밀번호 P가 123 이고 주어지는 번호 K가 100 일 때, 100부터 123까지 24번 확인하여 비밀번호를 맞출 수 있다.

P와 K가 주어지면 K부터 시작하여 몇 번 만에 P를 맞출 수 있는지 알아보자.


**[입력]**

입력으로 P와 K가 빈 칸을 사이로 주어진다.


**[출력]**

몇 번 만에 비밀번호를 맞출 수 있는지 출력한다.

- 입력

```
123 100
```

- 출력

```
24
```

- solution

```python
# 비밀번호, 주어진 번호 input 생성
P, K = map(int, input().split())
# 확인 절차
print(abs(P - K) + 1)
```



## 2046. 스탬프 찍기

주어진 숫자만큼 # 을 출력해보세요.

주어질 숫자는 100,000 이하다.

- solution

```python
a = int(input())

print( '#' * a)
```



## 2047. 신문 헤드라인

신문의 헤드라인을 편집하기 위해, 주어지는 문자열의 알파벳 소문자를 모두 대문자로 바꾸는 프로그램을 개발 중이다.

입력으로 주어진 문장에 모든 소문자 알파벳을 찾아 대문자로 변환한 다음, 그 결과를 출력하는 프로그램을 작성하라.


**[예제 풀이]**

The_headline_is_the_text_indicating_the_nature_of_the_article_below_it.

위와 같은 문자열이 입력으로 주어졌을 때, 출력은 다음과 같다.

THE_HEADLINE_IS_THE_TEXT_INDICATING_THE_NATURE_OF_THE_ARTICLE_BELOW_IT.


**[제약 사항]**

문자열의 최대 길이는 80 bytes 이다.


**[입력]**

입력으로 80 bytes 이하의 길이를 가진 문자열이 주어진다.


**[출력]**

문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.

- solution

```python
# input str 확인
str = input()

print(str.upper())
```



## 2050. 알파벳을 숫자로 변환

알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.


**[제약 사항]**

문자열의 최대 길이는 200이다.


**[입력]**

알파벳으로 이루어진 문자열이 주어진다.


**[출력]**

각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.

- solution

```python
words = input()
numbers = []

# 단어 string 생성
strings = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# string 안에 index 위치 확인해서 + 1 한 뒤 숫자 반환
for word in words:
    if word in strings:
        numbers.append(strings.index(word) + 1)
# string 형태로 출력하기 위한 형변환 필요 list내의 int => str
print(' '.join(map(str,numbers)))
```

- example solution

```python
# ascii 이용
for c in input():
    print( ord(c)-64, end=' ' )
```



## 1979. 어디에 단어가 들어갈 수 있을까

- 어려웠던 점

행과 열별로 연속된 경우 & 정확히 길이가 일치하는 경우만 단어가 들어갈 수 있기 때문에 여러 가지 케이스 제한 사항이 존재했음 => 이를 조건으로 모두 넣어줘야 했기에 어려움이 존재

example

<만족하는 경우의 수>

1의 수가 K랑 같아졌고 뒤에 0을 만나는 case

1의 수가 K랑 같아졌고 맨 마지막 탐색을 끝내서 만족하는 case