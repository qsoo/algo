## 231. 함수3 - 형성평가1

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=131&sca=10d0)

1회독: 21.06.01



### my solution

```python
N = int(input())

# 재귀 함수
def recur(target: int, arr: list) -> list:
    # 종료 조건
    if target == 1:
        print(*arr)
        return
    else:
        # 1. 맨 처음 인덱스에 // 2 값 넣어주기
        arr.insert(0, target//2)
        recur(target//2, arr)
recur(N, [N])
```

