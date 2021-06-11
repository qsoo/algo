## 187. 문자열1 - 형성평가6

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=87&sca=10e0)

1회독: 21.06.11



### my solution 1

```python
# 리스트로 변형
target = list(input().strip())
while True:
    idx = int(input().strip()) - 1
    if len(target) <= idx:
        del target[-1]
    else:
        del target[idx]
    print(''.join(target))
    # 조건 만족 break
    if len(target) == 1:
        break
```

리스트로 변형해서 

(1) 리스트의 해당 index를 지워준다(del or pop or remove 사용) - del과 remove가 좀 더 빠르다

(2) out of index 에러를 막기 위해 현재 길이보다 크거나 같으면 -1 index를 삭제 

(3) 길이가 1이면 break 단, len(str)을 마지막에 종료 조건에서 직접 계산해야 한다

​	미리 변수에 담아 놓으면 변경사항이 적용되지 않음 

​	∵ 조작을 직접 가하기 때문에 변형된 후에 직접 계산을 해야 함

### my solution 2

```python
# 문자열 그대로
str = input().strip()
while True:
    idx = int(input().strip()) - 1
    # 문자열 index 범위 넘는지 확인
    if len(str) <= idx:
        str = str[:-1]
    else:
        str = str[:idx] + str[idx + 1:]
    print(str)
    if len(str) == 1:
        break
```



### 참고 자료

- `remove(value)` : 값을 찾아 첫 번째로 나오는 값을 삭제

- `clear()` : 리스트의 모든 값 삭제

- `del()` : index을 지정하여 삭제 가능, -1(마지막 값), out of range있음

  example) del list[-1]

- `pop()` : index 생략 시 마지막 값 삭제(stack - LIFO)



### 태그

- 문자열
- 리스트