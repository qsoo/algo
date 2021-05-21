## 42839. 소수찾기

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42839)

1회독: 20.12.09



### Idea

전체 문자열(length=N이라 할 때)로 만들 수 있는 수들을 찾아야한다. 

(1) N 개 중 1, 2, 3 .... N 개를 뽑은 다음 

(2) 뽑은 개수로 만들 수 있는 순열을 만들고 

(3) 소수인지 판별 하는 흐름으로 이동한다. 

순열을 만드는 함수를 만들 때 몇 개를 뽑아서 만들 것인지와 중복 처리 부분을 이해하지 못함 ⇒ 다시 봐야함



#### my solution

```python
def permutation(arr, r, result):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]



    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            # shallow copy이기 때문에 이를 변수에 저장
            temp = chosen[:]
            temp = ''.join(temp)
            # 중복 제거
            if temp != '':
                temp = int(temp)
								# 중복 제거를 위한 조건
                if temp not in result:
                    result.append(temp)
            return

        for i in range(len(arr)):
            # 3.
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return result

def check_prime(arr, count):
    for i in arr:
        target = i
        # 소수는 1보다 크다
        if 2 < target:
            for j in range(2, target):
                # 나누어 떨어지지 않는다
                if target % j == 0:
                    is_prime_number = False
                    break
                else:
                    is_prime_number = True

            if is_prime_number:
                count += 1

        elif target == 2:
            count += 1

    return count


def solution(numbers):
    count = 0
    # 순열 저장할 배열
    result = []
    for i in range(len(numbers) + 1):
        permutation(numbers, i, result)

    return check_prime(result, count)
```



### 태그

- 순열