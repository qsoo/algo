## 185. 문자열1 - 형성평가4

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=85&sca=10e0)

1회독: 21.06.11



### my solution 1

```python
# 일반적인 방법
target, find_str = input().split()
# 찾을 index
i = 0
find_flag = False
for x in target:
    if x == find_str:
        print(i)
        find_flag = True
        break
    i += 1
if not find_flag:
    print('No')
```



### my solution 2

```python
# enumerate 사용
target, detect = input().split()
# 0. 찾는 문자 없을 때
flag = True
# 1. enumerate 사용위해 list로 변경
for idx, val in enumerate(list(target)):
    if val == detect:
        print(idx)
        flag = False
        break
# 2. 찾는 문자 없을 때
if flag: print('No')
```



### 태그

- 문자열
- enumerate