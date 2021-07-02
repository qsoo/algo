## 211. 파일입출력 - 형성평가7

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=111&sca=10i0)

1회독: 21.07.02



### Idea

윤년 구하는 법

1. 4로 나눠떨어지고 100으로 나눠떨어지지 않는 해

2. 100으로 나눠떨어지고 400으로도 나눠떨어지는 해

   (4와 100으로 나눠떨어지지만 400으로 나눠떨어지지 않으면 평년)



### my solution

```python
# 윤년: 100으로 나눠지지 않고 4로 나누어 떨어지는 해, 100으로 나누어지고 400으로 나눠지는 해
a, b = map(int, input().split())
temp = 0
for i in range(a, b + 1):
    if not (i % 4) and (i % 100):
        temp += 1
    elif not (i % 100) and not (i % 400):
        temp += 1

print(temp)
```



### 태그

- 윤년
- 조건문