## 1341. 구구단 2

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2076&sca=20)

1회독: 21.09.03



### Idea

조건에 따라 (start < end or start > end) 증가와 감소가 다르므로  

1. range(start, end, step)에서 step에 변수를 할당하여 조건에 따라 증가폭을 다르게 주고
2. 출력 형식에 따라 format을 맞춰준다



### my solution

```python
s, e = map(int, input().split())
epoch = 1
if s > e: epoch = -1

for i in range(s, e + (epoch), epoch):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j:>2}', end ='   ')
        if not (j % 3):
            print()
    print()
```



### 태그

- for문
- f-string