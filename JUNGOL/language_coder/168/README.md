## 168. 배열2 - 형성평가9

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=68&sca=10a0)

1회독: 20.12.29



### my solution 1

```python
n = int(input().strip())
# 1. 기본 뼈대 만들기
pascal = [[0] * (i + 1) for i in range(n)]

# 2. 맨 첫 항 값 1로 바꿔주기
pascal[0][0] = 1

for i in range(1, n):
    for j in range(len(pascal[i])):
        # 3. 양 끝의 값 == 1
        if not j or j == i:
            pascal[i][j] = 1
        # 4. 나머지 값의 규칙 : nCr = n-1Cr-1 + n-1Cr
        else:
            pascal[i][j] = pascal[i-1][j - 1] + pascal[i - 1][j]

for i in range(len(pascal) - 1, -1, -1):
    print(*pascal[i])
```



### (참고) 재귀를 이용한 pascal triangle

### my solution 2

```python
def pascal(n, k):
		if n == k:
				return 1
		elif k == 1:
				return 1
		else:
				return pascal(n-1, k) + pascal(n-1, k-1)
```



### my solution 3

```python
# pascal triangle

def calculate(prev):
    res = [0]*(len(prev)+1)
    res[0], res[-1] = 1, 1
    for i in range(0,len(res)):
        if res[i] == 0:
            res[i] = prev[i-1] + prev[i]
    return res


def RecPascal(n, m=0, prev=[]):
    if m > n:
        return []
    elif m == 0:
        return RecPascal(n, m+1 , [1])
    else:
        return [prev] + RecPascal(n, m+1, calculate(prev))
```



### 태그

- 배열
- 파스칼 삼각형