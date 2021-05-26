## 145. 반복제어문3 - 형성평가6

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=45&sca=1080)

1회독: 20.12.16



### Idea

문자열을 왼쪽에는 공백을 두고 오른쪽에 출력하기



### my solution

```python
n = int(input())
temp = ''
# 맨 밑에 출력할 문자열부터 만들어준다
for i in range(1, n+1):
    temp += str(i) + ' '
# 맨 밑에 출력할 문자열에서 마지막 공백 제거
temp = temp.rstrip(' ')
result = []
for i in range(n, 0, -1):
    replace_target = str(i)
    replace_boundary = len(str(i)) + 1
    result.append(temp)
    # 왼쪽 공백 추가하기
    temp = (' '*2) + temp[:-replace_boundary]
result.sort()
for i in range(len(result)):
    print(result[i])
```



### 참고 코드

https://battlewithmyself.tistory.com/58

```python
num = int(input())

for i in range(1, num+1):
  for j in range(num-i):
      print(" ", end=' '),
  for k in range(1, i+1):
      print("{} ".format(k), end=''),
  print("")
```



### (틀린 코드)

```python
n = int(input())
range_str = 2*n - 1
for i in range(1, n+1):
    temp = ''
    for j in range(1, i+1):
        temp += ' ' + str(j)
        if j == 1:
            temp = temp.lstrip(' ')
    print(temp.rjust(range_str))
```

숫자가 10이상이 되면 두 칸씩 차지하게 되어 주어진 조건에 맞지 않게 된다.



### 태그

- 문자열 정렬
- 출력