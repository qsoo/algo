## 512. 입력 - 자가진단 4

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=149&sca=1020)

1회독: 20.12.09



### Idea

소수점 자릿수를 표현해주는 것이 point! 

example) 13.1467 ⇒ 13.146700 형식으로 출력



### my solution

```python
sinker = 49
gravity = 0.268300

# 자릿수 맞춰주기
result = sinker * gravity
print("{} * {} = {:.6f}".format(sinker, gravity, result))
```



### 참고 자료

```python
# format 메서드
{인덱스:0개수d}.format(숫자)

# example 1 integer의 경우
'{0:03d}'.format(35)
>> '035'

# example 2 float의 경우 - 자릿수를 표현하는 것이기 때문에 뒤에는 버림 처리
{인덱스:0개수.자릿수f}.format(숫자)

'{0:06.2f}'.format(35)
>> '035.00'

# 주의할 점: 실수는 숫자 개수에 정수부분 + 소수점 + 소수점 이하 자릿수 포함
# 즉, 위의 예에서 3(정수부 자릿수) + 1(소수점) + 2(소수점 이하 자릿수) == 6
```



### 태그

- 출력