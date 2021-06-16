## 611. 문자열2 - 자가진단A

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=248&sca=10f0)

1회독: 21.06.16



### my solution

```python
# 1. 문자열로 입력
string = input().strip()
result = ''
# 1 - 1. 끝까지 진행했는데 에러 발생하지 않으면 모두 실수부
is_float = False
# 2. 문자열 체크를 통해 실수부 변환 가능한 부분만 가져오기
for i in range(2, len(string) + 1):
    temp = string[:i]
    # 실수 형태로 변환했을 때 작동하는 지 확인
    try:
        float(temp)
        is_float = True
    except:
        result = float(string[:i-1])
        is_float = False
        break
if is_float:
    result = float(string)
print(int(result * 2))
print('{:.2f}'.format(round(result, 2)))
```

주어진 문자열을 탐색하면서 

(1) 현재까지의 slicing된 부분이 실수로 변환 가능한지 체크하고 

(2) 변환이 안된다면 이 전 인덱스 위치까지가 변환되는 지점 

(3) for문을 빠져나올 때까지 에러가 발생하지 않으면 모든 문자열이 실수 

(4) 형식에 맞게 출력



### (틀린 코드)

```python
# 1. 문자열로 입력
string = input().strip()
result = ''
is_flag = True
# 2. 문자열 체크를 통해 실수부 변환 가능한 부분만 가져오기
for i in range(len(string) - 1):
    temp = string[i]
    next = string[i + 1]
    # 2 - 0. 숫자형인지 판별
    try:
        int(temp)
        is_flag = False
    except:
        # 2 - 1. 소수점 표현하는 '.'이면 진행
        if temp == '.':
            try:
                int(next)
            # 숫자형이 안될 때는 stop
            except:
                result = float(string[:i])
                is_flag = True
                break
            # 숫자형으로 변환 가능하면 진행 계속
 
            # 2 - 2. 현재까지의 숫자 담기
        else:
            result = float(string[:i])
            is_flag = True
            break
if not is_flag:
    result = float(string[:-1])
 
print(int(result) * 2)
print('{:.2f}'.format(round(result, 2)))
```

통과는 했으나 논리 구조를 다시 생각해보니 '10.3.3.3' 같은 경우는 걸러주지 못함



### 태그

- 문자열
- 에러문
- 형변환