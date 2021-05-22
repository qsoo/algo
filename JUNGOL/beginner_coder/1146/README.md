## 1146. 선택정렬

[문제 링크](http://jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=426&sca=2070)

1회독: 20.12.20



### Idea

선택정렬 

1. 주어진 수열 중에 최소값(같은 값이 여러 개 있는 경우 처음 값)을 찾는다. 
2. 찾은 최소값을 맨 앞의 값과 자리를 바꾼다. 
3. 맨 앞의 값을 뺀 나머지 수열을 같은 방법으로 전체 개수-1번 반복 실행한다.

시간복잡도 

$O(n) = n^2$



### my solution

```python
n = int(input().strip())

arr = list(map(int, input().split()))

# 1. 총 길이만큼 반복을 수행한다
i = 0
while i < n - 1:
    # 0 <= in arr <= 100 이므로
    target = 101
    # 2. 가장 작은 값을 찾아서 위치를 맨 앞과 교환
    for j in range(i,n):
        if arr[j] < target:
            target = arr[j]
            idx = j

    # 3. 찾은 가장 작은 값을 맨 앞으로 이동시킨다
    arr[i], arr[idx] = arr[idx], arr[i]

    i += 1

    for k in range(n):
        print(arr[k], end=' ')
    print()
```



### (참고사항)

```python
# *(asterisk)의 활용용도

# 1. 곱셈 및 거듭제곱 연산
2 * 3
=> 6

# 2. 리스트형 컨테이너 타입의 데이터를 반복 확장할 때
zeros_list = [0] * 100

# 3. 가변인자를 사용할 때
def asterisk(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

asterisk('1', '2', '3', forth='helen', fifth='tom')

# ('1', '2', '3')
# <class 'tuple'>
# {'forth': 'helen', 'fifth': 'tom'}
# <class 'dict'>

# 4. container type의 데이터를 unpacking할 때 사용
arr = [1, 2, 3, 4]

print(*arr)
# 1, 2, 3, 4
```

[참고 링크](https://mingrammer.com/understanding-the-asterisk-of-python/)



### 태그

- 정렬
- 선택정렬