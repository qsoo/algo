## 1141. 불쾌한 날

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=421&sca=3020)

1회독: 21.02.25



### (틀린 코드)

#### my solution 1

```python
# N: 소들의 수
N = int(input().strip())
# 소들의 배열
arr = [int(input().strip()) for i in range(N)]

# 최종 결과값
result = 0

for i in range(N-1):
    for j in range(i+1, N):
        if arr[i] > arr[j]:
            result += 1
        else:
            break

print(result)
```

#### my solution 2

```python
import sys
N = int(sys.stdin.readline().strip())

# 소들의 배열
arr = []
# 결과값 저장
result = 0
for _ in range(N):
    # 현재 들어오는 소
    cow = int(sys.stdin.readline().strip())

    # 비어있으면 바로 넣는다
    if not arr:
        arr.append(cow)
    # 비어 있지 않으면 현재 들어오는 것보다는 작은 애들은 다 없앤다
    else:
        i = 0
        while i < len(arr):
            if arr[i] <= cow:
                arr.pop(i)
            else:
                i += 1
                result +=1

        arr.append(cow)

print(result)
```

이중 반복문을 통해 해결하는 기본 문제인지 알았지만  

전체적으로 시간초과를 해결하는 게 key point인 문제 

최대한 반복 횟수를 줄여야(문제에서 주어진 시간 1초) 시도해 본 리스트 

(1) 이중 for문 

(2) 퀵 정렬을 응용(pivot - 최대 크기로 설정) 

(3) stack을 이용해서 작은 값은 담지 않는 방식으로 리스트의 길이를 줄임 

결과적으로 모두 실패



### 태그

- 탐색