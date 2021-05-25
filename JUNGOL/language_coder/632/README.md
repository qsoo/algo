## 632. 선택제어문 - 자가진단9

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=660&sca=1050)

1회독: 20.12.10



### Idea

삼항연산자를 사용하여 간결한 코드 작성을 시도



### my solution

```python
a, b, c = map(int, input().split())

print( c if c < (a if a < b else b) else (a if a < b else b))
```



### 참고 자료

```python
# 삼항 연산자
#  조건이 True일 때 보여줄 값 if 조건문 else 조건이 false일 때 보여줄 값

# 위의 예제에서
# True => a, False => b
a if a < b else b    # 1단계 a와 b 중 작은 값이 나온다

# 2단계 True => c False => a와 b 중 작은 값이 나옴
c if c < (a if a < b else b) else (a if a < b else b) 
```



### 태그

- 조건문
- 삼항연산자