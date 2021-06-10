## 236. 함수3 - 형성평가6

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=136&sca=10d0)

1회독: 21.06.08



### my solution 1

```python
# j, k, l
j, k, l = list(map(int, input().split()))


# 각 자릿수 곱 구하기
def mul(target:int, result:int):
    # 1. 각 자리수의 곱
    multiple_target = target % 10
    # 종료 조건
    if not target:
        return result
    elif multiple_target:
        result *= multiple_target
    return mul(target // 10, result)


print(mul((j * k * l), 1))
```

밑에 함수를 두 개 써서 만든 부분을 한 개로 변경하고 

global 선언을 함수 내부적으로 변경



### my solution 2

```python
# j, k, l
arr = list(map(int, input().split()))
result = 1


# 각 자릿수 곱 구하기
def mul(target):
    global result
    # 1. 각 자리수의 곱
    multiple_target = target % 10
    # 종료 조건
    if not target:
        return result
    elif multiple_target:
        result *= multiple_target
    return mul(target // 10)


def multiple(j:int, k:int, l:int):
    global result
    # 1. 모든 수들의 곱
    temp = j * k * l
    # 2. 각 자리수 값
    return mul(temp)


print(multiple(*arr))
```

재귀 함수로 구현하기 위해 함수를 두 개 사용



### 태그

- 재귀