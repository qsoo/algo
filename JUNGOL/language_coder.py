'''
# N = list(map(int, input().split()))
N = [10, 25, 33]

print("sum : {}".format(sum(N)))
print("avg : {}".format(sum(N)//len(N)))

# 49 * 0.268300 = 13.146700

sinker = 49
gravity = 0.268300

# 자릿수 맞춰주기
result = sinker * gravity
print("{} * {:.6f} = {:.6f}".format(sinker, gravity, result))

print('{0:06.2f}'.format(35))

#  2.1yd = 192.0cm
# 10.5in =  26.7cm
#
# 1 yd = 91.44
# 1 in = 2.54

print(" {}yd = {:.1f}cm".format(2.1, (2.1*91.44)))
print("{}in =  {:.1f}cm".format(10.5, (10.5*2.54)))

input: height = 170
output: Your height is 170cm.

N = input("height = ")
print(type(N))
print("Your height is {}cm.".format(int(N)))

a, b = map(int, input().split())

print("{} * {} = {}".format(a, b, (a * b)))
print("{} / {} = {}".format(a, b, (a // b)))

a = float(input())
b = float(input())
string = input()

print("{:.2f}".format(a))
print("{:.2f}".format(b))
print(string)

for _ in range(3):
    temp = float(input())
    print(round(temp, 3))

a, b, c = 10, 20, 30

print("{} + {} = {}".format(a, b, c))
a = 80.5
b = 22.34

# print("{:>10.3d}{:>10}{:>10}".format(a, b, a+b))
c = 123
print("{:10.3f}".format(c))

print("{:>10.3f}".format(35))

a = int(50)
b = float(100.12)

print('{} * {} = {:.0f}'.format(b, a, a*b))

a, b, c = map(int, input().split())
sum = a + b + c
avg = int(sum / 3)

print("sum = {}".format(sum))
print("avg = {}".format(avg))

N = float(input("yard? "))
print("{}yard = {:.1f}cm".format(N, round(N*91.44, 1)))

a, b = map(int, input().split())
a += 100
b %= 10

print(a, b)

a = int(input())
print(a)
print(a+2)

a, b = map(int, input().split())
b -= 1
result = a * b
a += 1
print(a, b, result)

a, b = map(int, input().split())
print(1 if a == b else 0)
print(0 if a == b else 1)

a, b = map(int, input().split())

print('{} > {} --- {}'.format(a, b, 1 if a > b else 0))
print('{} < {} --- {}'.format(a, b, 1 if a < b else 0))
print('{} >= {} --- {}'.format(a, b, 1 if a >= b else 0))
print('{} <= {} --- {}'.format(a, b, 1 if a <= b else 0))

a, b = map(int, input().split())
print(1 if a and b else 0, 1 if a or b else 0)

a, b, c = map(int, input().split())

print(1 if c < a and b < a else 0, end=' ')
print(1 if a == b == c else 0)
a, b, c, d = map(int, input().split())
print('sum {}'.format(a+b+c+d))
print('avg {}'.format((a+b+c+d) // 4))

a, b = map(int, input().split())

print('{0} / {1} = {2}...{3}'.format(a, b, a // b, a % b))

width, height = map(int, input().split())
width += 5
height *= 2
print('width = {}'.format(width))
print('length = {}'.format(height))
print('area = {}'.format(width*height))

a, b = map(int, input().split())
print(a+1, b)
print(a+1, b-1)

height_a, weight_a = map(int, input().split())
height_b, weight_b = map(int, input().split())
print(1 if height_b < height_a and weight_b < weight_a else 0)

a, b = map(float, input().split())
print(int(a*b), int(a)*int(b))

a, b = map(int, input().split())
print('{} {:.2f}'.format(a//b, round(float(a) / b, 2)))

ex = list(map(float, input().split()))
int_sum = 0
float_sum = 0
for i in range(len(ex)):
    int_sum += int(ex[i])
    float_sum += ex[i]

print('sum {}'.format(int_sum))
print('avg {:.0f}'.format(float_sum//len(ex)))

a = 5
a += 10
a = a - 1
print (a)

from datetime import datetime

now = datetime.now()
a = 0
a = now.year - 1900 # p
a += now.month - 1  # q
a += now.day

print(0, 120, 141)      # r

a = int(input())
print(a)
if a < 0:
    print('minus')
a, b = map(int, input().split())
ratio = b+100-a
print(ratio)
if ratio > 0:
    print('Obesity')

age = int(input())

if 20 <= age:
    print('adult')
else:
    print('{} years later'.format(20 - age))

a = float(input())

if a <= 50.80:
    print('Flyweight')
elif 50.80 < a <= 61.23:
    print('Lightweight')
elif 61.23 < a <= 72.57:
    print('Middleweight')
elif 72.57 < a <= 88.45:
    print('Cruiserweight')
else:
    print('Heavyweight')


a, b = map(float, input().split())
if 4 <= a and 4 <= b:
    print('A')
elif 3 <= a and 3 <= b:
    print('B')
else:
    print('C')

sex, age = map(str, input().split())
age = int(age)

if sex == 'M':
    if 18 <= age:
        print('MAN')
    else:
        print('BOY')

elif sex == 'F':
    if 18 <= age:
        print('WOMAN')
    else:
        print('GIRL')

a = input().strip()

if a == 'A':
    print('Excellent')
elif a == 'B':
    print('Good')
elif a == 'C':
    print('Usually')
elif a == 'D':
    print('Effort')
elif a == 'F':
    print('Failure')
else:
    print('error')

a = float(input())

if 4 <= a:
    print('scholarship')
elif 3 <= a:
    print('next semester')
elif 2 <= a:
    print('seasonal semester')
elif a < 2:
    print('retake')

a, b, c = map(int, input().split())

print( c if c < (a if a < b else b) else (a if a < b else b))


a, b = map(int, input().split())
print(abs(a-b))
print(a - b if b < a else b - a)

a = int(input())

if 0 < a:
    print('plus')
elif a < 0:
    print('minus')
else:
    print('zero')

a = int(input())
if not a % 400:
    print('leap year')
elif not a % 4 and a % 100:
    print('leap year')
else:
    print('common year')

if not a % 400 or (not a % 4 and a % 100):
    print('leap year')
else:
    print('common year')

print('leap year' if not a % 400 or (not a % 4 and a % 100) else 'common year')
a = input('Number? ').strip()

if a == '1':
    print('dog')
elif a == '2':
    print('cat')
elif a == '3':
    print('chick')
else:
    print('I don\'t know.')

a = int(input())
date = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(date[a])

i = 1

while i <= 15:
    print(i, end=' ')
    i += 1

a = int(input())

i = 1
result = 0
while i <= a:
    result += i
    i += 1
print(result)

while 1:
    a = int(input('number? '))
    if a > 0 :
        print('positive integer')
    elif a < 0:
        print('negative number')
    else:
        break
target = list(map(int, input().split()))

temp = 0
for i in range(len(target)):
    temp += target[i]
    if 100 <= target[i]:
        print(temp)
        print(round(temp / (i+1), 1))

while 1:
    target = int(input())
    if not target % 3:
        print(target // 3)
    elif target == -1:
        break

country_dict = {
    1: ['1. Korea', 'Seoul'],
    2: ['2. USA', 'Washington'],
    3: ['3. Japan', 'Tokyo'],
    4: ['4. China', 'Beijing'],
}

while 1:
    for i in range(1, len(country_dict)+1):
        print(country_dict[i][0])
    a = int(input('number? '))
    print()
    if not (1 <= a <= 4):
        print('none')
        break
    print(country_dict[a][1])
    print()

a = int(input())
i = 1
while i <= a:
    print(i, end=' ')
    i += 1

num_li = list(map(int, input().split()))

for i in range(len(num_li)):
    if num_li[i] == 0:
        temp = i
        break

num_li = num_li[:temp]
odd, even = 0, 0
for i in range(len(num_li)):
    if num_li[i] % 2:
        odd += 1
    else:
        even += 1

print('odd : {}'.format(odd))
print('even : {}'.format(even))

num_li = list(map(int, input().split()))
is_True = True

num_sum = 0
i = 0
while is_True:
    if not (0 <= num_li[i] <= 100):
        print('sum : {}'.format(num_sum))
        print('avg : {}'.format(round(num_sum / i, 1)))
        is_True = False
    else:
        num_sum += num_li[i]
        i += 1
li = list(map(int, input().split()))
i = 0
cnt = 0
while li[i] != 0:
    if li[i] % 3 and li[i] % 5:
        cnt += 1
    i += 1

print(cnt)

flag = "Y"
while flag == 'Y' or flag == 'y':
    w = int(input('Base = '))
    h = int(input('Height = '))
    print('Triangle width = {}'.format(round(w*h / 2, 1)))
    flag = input('Continue? ').strip()

x = int(input().strip())
temp = 0
# for i in range(x, 101, 1):
#     temp += i

for i in range(100, x-1, -1):
    temp += i
print(temp)

arr = list(map(int, input().split()))

result = [0, 0]
for i in range(len(arr)):
    if not arr[i] % 3:
        result[0] += 1
    if not arr[i] % 5:
        result[1] += 1

print('Multiples of 3 : {}'.format(result[0]))
print('Multiples of 5 : {}'.format(result[1]))

N = int(input().strip())
score = list(map(int, input().split()))
total = 0
for i in range(N):
    total += score[i]
avg = round(total / N, 1)
print(f'avg : {avg}')
print('pass') if avg >= 80 else print('fail')

for i in range(5):
    for j in range(5):
        print(i+j+2, end=' ')
    print()

for i in range(2, 5, 1):
    for j in range(1, 6, 1):
        print(f'{i} * {j} = {i * j:>2}', end='   ')
    print()

N = int(input().strip())
print('JUNGOL\n'*N, )
a, b = map(int, input().split())
if a > b:
    for i in range(b, a + 1):
        print(i, end=' ')
else:
    for i in range(a, b + 1):
        print(i, end=' ')

N = int(input().strip())
temp = 0
for i in range(5, N+1, 5):
    temp += i
print(temp)
N = int(input().strip())
arr = list(map(int, input().split()))
total = 0
for i in range(N):
    total += arr[i]
print('{}'.format(round(total/N, 2)))

arr = list(map(int, input().split()))
result = [0, 0]
for i in range(10):
    if arr[i] % 2:
        result[0] += 1
    else:
        result[1] += 1
print('even : {}'.format(result[1]))
print('odd : {}'.format(result[0]))
a, b = map(int, input().split())
temp, cnt = 0, 0
if b < a:
    a, b = b, a

for i in range(a, b+1):
    if (not i % 3) or (not i % 5):
        temp += i
        cnt += 1

print('sum : {}'.format(temp))
print('avg : {}'.format(round(temp/cnt, 1)))

N = int(input().strip())
for i in range(1, 11):
    print(N * i, end=' ')

y, x = map(int, input().split())
for i in range(y):
    for j in range(x):
        print((i+1)*(j+1), end=' ')
    print()

N = int(input().strip())
for i in range(N):
    for j in range(N):
        print((i+1, j+1), end=' ')
    print()

a, b = map(int, input().split())

if a > b:
    for j in range(1, 10):
        for i in range(a, b-1, -1):
            print(f'{i} * {j} = {i * j:>2}', end='   ')
        print()
else:
    for j in range(1, 10):
        for i in range(a, b+1):
            print(f'{i} * {j} = {i * j:>2}', end='   ')
        print()

arr = [1, 2, 3]

def cal():
    for i in range(len(arr)):
        for j in range(len(arr)):
            print('{} + {} = {}'.format(arr[i], arr[j], arr[i] + arr[j]))

cal()


def bubble_sort():
    for i in range(len(arr) -1, 0, -1):
        for j in range(i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(*arr)

arr = list(map(int, input().split()))
bubble_sort()


a, b = map(int, input().split())

def cal(a:int, b:int) -> int:
    print('({} - {}) ^ 2 = {}'.format(a, b, (a - b) ** 2 ))
    print('({} + {}) ^ 3 = {}'.format(a, b, (a + b) ** 3 ))

cal(a, b)


n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
print(*arr)

import math
a, b = map(float, input().split())

# 내림차순 정렬
if a < b:
    a, b = b, a

def cal(a, b):
    a = math.sqrt(a)
    b = math.sqrt(b)

    c, d = int(a), int(b)
    result = c - d

    if b == d:
        result += 1

    return result


print(cal(a, b))


arr = list(map(lambda x: abs(int(x)), input().split()))

print(sum(arr))

arr = list(map(float, input().split()))

def avg(arr:list) -> tuple:
    # 1. 평균 -> 반올림
    total_1 = int(round(sum(arr) / len(arr), 0))
    # 2. 반올림 -> 평균
    total_2 = int(round(sum(list(map(lambda x : round(x, 0), arr))) / len(arr), 0))

    print(total_1)
    print(total_2)

avg(arr)


arr = list(map(int, input().split()))

def bubble_sort(arr):
    for _ in range(3):
        for i in range(0, len(arr) - 1, 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    print(*arr)

bubble_sort(arr)
pi = 3.141592
r = float(input('radius : '))

def cal_area(r):
    print('area = {}'.format(round(r ** 2 * pi, 3)))

cal_area(r)
N = int(input())

def recur(n):
    if n == N:
        return
    print('recursive')
    n += 1
    recur(n)

recur(0)

N = int(input())

def recur(n):
    if n == 0:
        return
    print(n, end=' ')
    n -= 1
    recur(n)

recur(N)

N = int(input())

def recur(n, total):
    if n == 0:
        return total

    return recur(n-1, total + n)

print(recur(N, 0))

n = int(input())
a = 0
def recur1(n):
    global a
    # 종료조건
    if n < 10:
        a += n**2
        return
    a += (n % 10) ** 2
    n = n // 10
    recur1(n)

recur1(n)
print(a)

def recur(n):
    if n == 0:
        return 0

    return (n % 10) ** 2 + recur(n // 10)

print(recur(n))

N = int(input())
combi = [1]*(N+1)    # 하나의 조합 저장 배열 (0번 인덱스는 사용 안함)

def dfs(depth):
    if depth > N:         # 한 조합 생성 완료
        print(*combi[1:]) # 0번 제외하고 출력하고 돌아감
        return
    for i in range(1, 7): # 1~6 (주사위 눈) 재귀 호출
        if combi[depth - 1] <= i:
            combi[depth] = i # 호출전, 조합 배열에 값 추가
            dfs(depth+1)

dfs(1)


N = int(input())
arr = [0, 1]

def comb(n:int)-> int:
    # 종료 조건
    if n == N + 1:
        print(arr[-1])
        return

    temp = arr[n//2] + arr[n - 1]
    arr.append(temp)
    comb(n+1)

comb(2)


N = int(input())

# 재귀 함수
def recur(target: int, arr: list) -> list:
    # 종료 조건
    if target == 1:
        print(*arr)
        return
    else:
        # 1. 맨 처음 인덱스에 // 2 값 넣어주기
        arr.insert(0, target//2)
        recur(target//2, arr)
recur(N, [N])



N = int(input())
arr = [N]
def check_odd_even(n: int) -> list:
    # 0. 종료조건
    if n <= 2:
        print(*arr)
        return
    else:
        arr.insert(0, n - 2)
        check_odd_even(n - 2)

check_odd_even(N)

N, M = map(int, input().split())

def recur(n: int, arr: list, sumVal: int):
    # print(n, m, arr)
    # 1. 종료 조건 추가 - 값이 더 클 때
    if sumVal > M:
        return
    # 1. 종료조건
    elif n == N:
        # 2. 출력 조건
        if sumVal == M:
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            recur(n + 1, arr + [i], sumVal+i)

recur(0, [], 0)

N, M = map(int, input().split())

def recur(n: int, arr: list, sumVal: int):
    # 1. 종료조건
    if n == N:
        if sumVal == M:
            # 2. 출력 조건
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            recur(n + 1, arr + [i], sumVal+i)

def recur2(n: int, arr: list, sumVal: int):
    # 1. 종료조건
    if n == N:
        if sumVal == M:
            # 2. 출력 조건
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            if sumVal + i > M:
                break
            recur(n + 1, arr + [i], sumVal+i)
        return
# 시간 측정 추가
import time

start = time.time()  # 시작 시간 저장

# 작업 코드
recur2(0, [], 0)


print("time :", time.time() - start)

N, M = list(map(int,input().split(' ')))
nums = [0] * N

def comb(depth, total):
    global nums

    if depth == N:
        if total == 0:
            print(*nums)
        return True

    for i in range(1,7):
        nums[depth] = i
        if total - i < 0 or (N-depth) * 6 < total:
            break
        comb(depth+1, total-i)

comb(0, M)


N = int(input().strip())
# 1. N의 크기에 맞는 배열 만들어 주기 - 해당 인덱스에 저장하겠다
arr = [0 for _ in range(N + 1)]
arr[1] = 1
arr[2] = 2
def recur(n: int) -> int:
    # 1. 종료 조건 설정
    if n <= 2:
        return n
    else:
        return recur(n - 2) * recur(n - 1) % 100

print(recur(N))

N, M = map(int, input().split())

def recur(n: int, arr:list, sumVal: int):
    # 1. 종료조건
    if n == N:
        if sumVal == M:
            # 2. 출력 조건
            print(*arr)
        return
    else:
        # 2. 주사위 값 넣어주기
        for i in range(1, 7):
            # 가지 치기 부분에 다음 값들 최대(6일 때)여도 지정한 M보다 작을 때 추가
            if sumVal + i > M or (N - n) * 6 < M - (sumVal + i):
                break
            recur(n + 1, arr + [i], sumVal + i)
        return

recur(0, [], 0)

N = int(input().strip())
# 1. N의 크기에 맞는 배열 만들어 주기 - 해당 인덱스에 저장하겠다
arr = [0 for _ in range(N)]
arr[0] = 1
arr[1] = 2


def recur(n: int) -> int:
    # 1. 종료 조건 설정
    if n == N - 2:
        return arr[-1]
    else:
        arr[n + 2] = arr[n] * arr[n + 1] % 100
        return recur(n + 1)

print(recur(0))


N = int(input().strip())

def recur(target:int, depth:int):
    # 종료 조건
    if target == 1:
        return depth

    # 나누기
    elif (target % 2):
        return recur(target // 3, depth + 1)
    else:
        return recur(target // 2, depth + 1)

print(recur(N, 0))

# j, k, l
j, k, l = list(map(int, input().split()))


# 각 자릿수 곱 구하기
def mul(target:int, result:int):
    # 1. 각 자리수의 곱
    multiple_target = target % 10
    # 종료 조건
    if not target:
        return result
    elif multiple_target:
        result *= multiple_target
    return mul(target // 10, result)


print(mul((j * k * l), 1))

input = 66
ASCII code =? B
ASCII code =? z
ASCII code =?

# 1. input
while True:
    N = int(input('ASCII code =? '))
    if 33 <= N <= 127:
        print(chr(N))
    else:
        break

str = input()
print(str*2)

str = "Hong Gil Dong"
print(str[3:7])

string, N = input().split()
N = int(N)
for i in range(len(string) - 1, -1, -1):
    N -=1
    print(string[i], end='')
    if not N:
        break

a = ''
for i in range(2):
    a += input().strip()
print(len(a))

# 1. 65 <= X <= 122(문자)
# 2. 48 <= X <= 57(숫자)
while True:
    x = input().strip()
    temp = ord(x)
    if 65 <= temp <= 122:
        print(x)
    elif 48 <= temp <= 57:
        print(temp)
    else:
        break

target = input().strip()

for i in range(len(target)):
    temp = ord(target[i])
    # 1. 알파벳 걸러주기
    if 65 <= temp <= 90:
        print(target[i], end='')
    # 2. 소문자 대문자로 변환
    elif 97 <= temp <= 122:
        print(chr(temp - 32), end='')
    else:
        pass

target = list(input().split())
print(len(target))

str = input().strip()
length = len(str)
for i in range(1, (length + 1)):
    # 1. 오른쪽으로 밀었을 때 앞으로 오는 문자
    print(str[-i::] + str[:(length - i)])

# inline for문
a, b = [ord(temp) for temp in input().split()]
print(a + b, abs(a - b))

a, b = input().split()
a, b = ord(a), ord(b)
print(a + b, end=' ')
# if a > b:
#     print(a - b)
# else:
#     print(b - a)
print(a - b if a > b else b - a)

print(input()[:5])

# ASCII
# 32 ~ 64 특수문자
# 48 ~ 57 숫자
# 91 ~ 96 특수문자
# 122(z)

for i in input():
    temp = ord(i)
    # 알파벳, 숫자만
    if 48 <= temp <= 122:
        # 대문자이면 소문자로
        if 65 <= temp <= 90:
            print(i.lower(), end='')
        # 숫자, 소문자 그대로 출력
        elif 48 <= temp <= 57 or 97 <= temp <= 122:
            print(i, end='')

# 정규식 사용
import re
# 숫자 + 문자: '/w'에서 '_' 제외
num = re.compile('[a-zA-Z0-9]')

# findall
result = num.findall(input())
print("".join(x.lower() for x in result))

# 일반적인 방법
target, find_str = input().split()
# 찾을 index
i = 0
find_flag = False
for x in target:
    if x == find_str:
        print(i)
        find_flag = True
        break
    i += 1
if not find_flag:
    print('No')

# enumerate 사용
target, detect = input().split()
# 0. 찾는 문자 없을 때
flag = True
# 1. enumerate 사용위해 list로 변경
for idx, val in enumerate(list(target)):
    if val == detect:
        print(idx)
        flag = False
        break
# 2. 찾는 문자 없을 때
if flag: print('No')
arr = input().split()
print(len(arr[1]) if len(arr[0]) < len(arr[1]) else len(arr[0]))

# 리스트로 변형
target = list(input().strip())
while True:
    idx = int(input().strip()) - 1
    # 대상 문자열 길이
    length = len(target)
    if length <= idx:
        del target[-1]
    else:
        del target[idx]
    print(''.join(target))
    # 조건 만족 break
    if length == 1:
        break

# 문자열 그대로
str = input().strip()
while True:
    length = len(str)
    idx = int(input().strip()) - 1
    # 문자열 index 범위 넘는지 확인
    if length <= idx:
        str = str[:-1]
    else:
        str = str[:idx] + str[idx + 1:]
    print(str)
    if length == 1:
        break

arr = input().split()
for idx, val in enumerate(arr):
    print(f'{idx + 1}. {val}')

arr = input().split()
# for i in range(len(arr)):
#     print(f'{i + 1}. {arr[i]}')
print('\n'.join(f'{i + 1}. {arr[i]}' for i in range(len(arr))))

arr = []
while True:
    arr = [input()] + arr
    if len(arr) == 5:
        break

print('\n'.join(i for i in arr))


arr = input().split()

for i in range(len(arr)):
    if not i % 2:
        print(arr[i])
arr = []
for _ in range(10):
    arr.append(input().strip())
alphabet = input().strip()

# 1. 마지막 인덱스[-1]의 단어가 해당 alphabet과 같을 때 print
for i in range(10):
    if arr[i][-1] == alphabet:
        print(arr[i])
string = 'Hong Gil Dong'
print(string)

print(f"{input().strip()}fighting")

a, b = input().split()
print(f'{a[:2]}{b[2:]}{a[:2]}')
string = input().strip()

print("Yes" if "c" in string else "No", end=' ')
print("Yes" if "ab" in string else "No")

string = input().split()
result = []
for i in range(len(string) - 1, 0, -1):
    for j in range(len(string[i])):
        # 순서 뒤로 밀어주기(ord(i) > ord(i + 1)
        if ord(string[i - 1][j]) > ord(string[i][j]):
            string[i - 1], string[i] = string[i], string[i - 1]
            break
        # 순서 그대로
        elif ord(string[i - 1][j]) < ord(string[i][j]):
            break
        # 다음 알파벳 비교

print(string[0])
# 1. 5개 문자 입력받기
arr = []
for _ in range(5):
    arr.append(input().strip())
# arr = list(input().strip()) # 이런 식으로 쓰면 문자 하나씩 원소로 들어감['J','u' ...]

# 2. 문자열 역순 정렬(아마도 앞부터 순서 비교해서 숫자가 큰 값이 맨 앞으로 나오는 식)
for i in range(4):
    for j in range(0, 4 - i):
        # 3. 각 문자열의 수 구하기
        for k in range(len(arr[j])):
            if ord(arr[j][k]) < ord(arr[j + 1][k]):
                # 4. swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                break
            elif ord(arr[j][k]) > ord(arr[j + 1][k]):
                break

print('\n'.join(string for string in arr))
'''