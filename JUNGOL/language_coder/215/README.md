## 215. 문자열2 - 형성평가7

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=115&sca=10f0)

1회독: 21.06.28



### my solution

```python
# 0 - 48, 9 - 57 ascii 코드 기준
arr = input().split()
result = []
is_completed = False
for target in arr:
    for i in range(len(target)):
        ascii_code = ord(target[i])
        if ascii_code < 48 or ascii_code > 57:
            pivot = i
            is_completed = True
            break
    if not is_completed:
        pivot = len(target)
    # 마지막까지 or break문 만났을 때 전까지가 정수로 변환 가능
    result.append(int(target[:pivot]))

print(result[0] * result[1])
```



### (틀린 코드)

```python
# 0 - 48, 9 - 57 ascii 코드 기준
arr = input().split()
result = []
for target in arr:
    temp = ''
    for i in range(len(target)):
        if 48 <= ord(target[i]) <= 57:
            temp += target[i]
        else:
            result.append(int(temp))
            break
 
print(result[0] * result[1])
```

위와 같이 코드를 작성할 경우 `608`처럼 모두 정수부가 될 수 있는 문자열이 입력될 경우 

`result`에 아무것도 들어가지 않는 문제 발생

=> 해결 위해 flag를 추가



### 태그

- 문자열
- ASCII



