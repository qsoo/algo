# 1. 부분집합 만들기

ex = '0112'
ex = ['1', '2', '3']
cnt = 0
visited = [0, 0, 0]
def f(n, k):
    global cnt
    if n == k:
        for i in range(k):
            if visited[i] == 1:
                print(ex[i], end=' ')
        print()

    else:
        visited[n] = 1
        f(n+1, k)
        visited[n] = 0
        f(n+1, k)

# f(0, 3)
# def s(number):
#     exp = []
#     exp = list(map(str, number))
#     print(exp)
#
# number = '0123'
# s(number)

# 전체 원소와 순서를 가지는 순열 만들기
'''
def per(n):
    if n == 3:
        return
    else:
        b[n] = 1
        per(n+1)
        b[n] = 0
        per(n+1)

numb = ['1', '2', '3']
b = [0, 0, 0]


result = []

def permutation(arr, r):
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


numbers = '17'
for i in range(len(numbers)+1):
    permutation(numbers, i)
print(result)
# 2. prime number 검사
def check_prime(arr):
    global count
    for i in arr:
        target = i
        # 소수는 1보다 크다
        if target > 1:
            for j in range(2, target):
                # 나누어 떨어지지 않는다
                if target % j == 0:
                    is_prime_number = False
                    break
                else:
                    is_prime_number = True

            if is_prime_number:
                count += 1

    return
count = 0
check_prime(result)
print(count)
'''