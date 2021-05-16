## 14725. 개미굴

[문제링크](https://www.acmicpc.net/problem/14725)

1회독: 21.02.27



### Idea

string으로 전체 배열을 받아서 

(1) 사전순 정렬을 위해 sort를 시행해주고 

(2) 중복을 제거해주는 식으로 로직을 전개하면 된다 

이를 위해 그 전 원소와 현재 원소를 비교해서 

다른 지점이 나오면 해당 지점에서부터 모든 원소(현재 원소 - 리스트 내의 모든 원소)를 넣어주면 완성



### my solution

```python
# 먹이 정보 개수만큼
arr = []
for i in range(int(input())):
    temp = list(input().split())
    # '--' 붙여주기
    temp = temp[1:]
    for j in range(len(temp)):
        temp[j] = '--'*j + temp[j]

    arr.append(temp)

# 1. 사전 순서로 정렬
arr.sort()

# 결과값 저장할 변수
result = arr[0]

for i in range(len(arr) - 1):
    before = arr[i]
    after = arr[i + 1]
    for j in range(len(after)):
        # 2. j가 before의 원소의 개수보다 크면 추가
        if j > len(before):
            result.append(after[j])

        else:
            # 같지 않으면(여기서부터 다) 추가해줘야 함
            if before[j] != after[j]:
                for k in range(j, len(after)):
                    result.append(after[k])
                break

for i in range(len(result)):
    print(result[i])
```



### 태그

- 트리