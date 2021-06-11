## 182. 문자열1 - 형성평가1

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=82&sca=10e0)

1회독: 21.06.11



### my solution

```python
# inline for문
a, b = [ord(temp) for temp in input().split()]
print(a + b, abs(a - b))

# 기존의 방식
a, b = input().split()
a, b = ord(a), ord(b)
print(a + b, end=' ')
if a > b:
    print(a - b)
else:
    print(b - a)
    
# 삼항 연산자
a, b = input().split()
a, b = ord(a), ord(b)
print(a + b, end=' ')
print(a - b if a > b else b - a)
```



### 참고 자료

#### python inline for or if

- for

  ```python
  # 기본 구조
  for i in v: 
  		for j in i: 
  			print(j) 
  
  # inline
  [j for i in v for j in i]
  ```

- if

  ```python
  # 기본 구조
  if x < 5:
  		print(0)
  elif x > 10:
  		print(1)
  else:
  		print(2)
  
  # inline
  print(0 if x < 5 else 1 if x > 10 else 2)



### 태그

- 문자열
- ASCII
- 삼항 연산자
- Inline for문