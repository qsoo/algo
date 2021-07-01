## 624. 포인터 - 자가진단6

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=261&sca=10h0)

1회독: 21.07.01



### my solution

```python
n = int(input())
arr = [0 for _ in range(n)]
arr = list(map(float, input().split()))
for i in arr:
    print('{0:0.2f}'.format(round(i, 2)), end=' ')
print()
print(f'hap : {round(sum(arr), 2):0.2f}')
print(f'avg : {round(sum(arr) / n, 2):0.2f}')
```

python으로 코드를 작성하게 되면 input을 받는 부분과 리스트 생성하는 부분 없애도 가능(~2 번째 줄)

소수 둘째자리까지 출력하기 위해 문자열 포매팅 이용한 것이 알고 넘어가야 하는 부분

`f'{target:0.2f}'`: 소수점 두 번째자리까지 표시



### 태그

- f-string
- 문자열 포맷팅