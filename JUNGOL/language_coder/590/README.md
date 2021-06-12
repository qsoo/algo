## 590. 함수3 - 자가진단5

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=227&sca=10d0)

1회독: 21.05.12



### my solution

```python
N = int(input())
combi = [1]*(N+1)    # 하나의 조합 저장 배열 (0번 인덱스는 사용 안함)

def dfs(depth):
    if depth > N:         # 한 조합 생성 완료
        print(*combi[1:]) # 0번 제외하고 출력하고 돌아감
        return
    for i in range(1, 7): # 1~6 (주사위 눈) 재귀 호출
        if combi[depth - 1] <= i:
            combi[depth] = i # 호출전, 조합 배열에 값 추가
            dfs(depth+1)

dfs(1)
```

dfs 느낌으로 재귀를 작성한 다음 이 전에 원소의 값을 기준으로 조건을 달아서 값을 넣어주면 되는 문제



### 태그

- 재귀