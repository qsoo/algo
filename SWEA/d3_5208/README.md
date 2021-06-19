## 5208. Electronic Bus 2

[문제 링크](https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do)

1회독: 20.11.03



### Idea

탐욕적 알고리즘으로 현재 내가 갈 수 있는 가장 먼 정류장(i번째)까지를 후보로 했을 때 

그 다음 정류장((i + 1)번째)을 더한 다음 가장 멀리 갈 수 있는 후보군을 추려서 진행

완전탐색으로는 어떻게 풀어야 할 지 모르겠다.



### my solution

```python
def change_num(stop:int, battery: int):
    # 1. battery 용량 확인 - 갈 수 있는 정류장의 인덱스 범위
    max_stop = stop + battery
    cnt = 0
    # 도착할 때까지 진행하겠다
    while max_stop < arr[0]:
        # 갈 수 있는 정류장 중 가장 합이 멀리 갈 수 있을 때 찾기
        max_length = 0
        for i in range(stop + 1, max_stop + 1):
            temp = arr[i] + i
            if max_length < temp:
                next_stop = i
                max_length = temp
        # 여기서 가장 큰 값을 찾아냈으니 확인
        # 충전 후 위치가 종점 도착이라면 끝
        if arr[0] <= next_stop:
            break
        
        # 다음 정류장으로 이동
        stop = next_stop
        max_stop = stop + arr[next_stop]
        cnt += 1

    # 최종 종료
    return cnt


for tc in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))

    # arr[0]: 정류장 수
    # 충전지 용량만큼 갈 수 있는 양이 있을 때 더했을 때 가장 큰 값 찾기
    result = change_num(1, arr[1])

    print('#{} {}'.format(tc, result))
```



### 태그

- 탐욕 알고리즘
- 백트래킹