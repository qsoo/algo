## 565. 배열2 - 자가진단2

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=202&sca=10a0)

1회독: 20.12.22



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



### (틀린 코드)

````python
arr = list(input().split())
tens = [0] * 10

for i in range(len(arr)):

    if arr[i] == '0':
        break
    temp = int(arr[i][0])
    tens[temp] += 1

for idx, val in enumerate(tens):
    if val:
        print(f'{idx} : {val}')
````

한자리 수 숫자의 경우에도 십의 자리수가 0인 것으로 개수를 세야한다. 

또한 위처럼 짜게 되면 한자리 수가 나왔을 때 일의자리수의 숫자가 몇 개인지 세는 코드



### 태그

- 배열