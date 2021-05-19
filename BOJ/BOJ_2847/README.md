## 2847. 게임을 만든 동준이

[문제 링크](https://www.acmicpc.net/problem/2847)

1회독: 21.03.05



### Idea

앞에서부터 확인하게 되면 10 9 9 같은 경우에는 7 8 9가 되야 되기 때문에 

다시 뒤로 돌아와서 이를 확인해줘야 하는 문제 발생 이를 해결하기 위해 

(1) 뒤에서부터 탐색 실시 

(2) 리스트의 요소들의 값을 변경 

리스트의 요소들의 값을 변경하지 않으면 

a1, a2, a3에서 a1에 a3의 변화가 반영되지 않는 문제가 발생할 수 있기 때문에 이를 반영해줘야 한다



### my solution

```python
# N: 레벨의 수
arr = []
for i in range(int(input())):
    arr.append(int(input().strip()))

# 1. 탐색하면서 크기가 크면 작게 만들어 준다
result = 0
for i in range(len(arr) - 1, 0, -1):
    if arr[i] <= arr[i - 1]:
        temp = arr[i - 1] - arr[i] + 1
        result += temp
        arr[i - 1] = arr[i] - 1

print(result)
```



### 태그

- 탐욕 알고리즘