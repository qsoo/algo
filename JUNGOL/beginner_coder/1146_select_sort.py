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
            # target = arr[j]
            idx = j

    # 3. 찾은 가장 작은 값을 맨 앞으로 이동시킨다
    arr[i], arr[idx] = arr[idx], arr[i]

    i += 1

    for k in range(n):
        print(arr[k], end=' ')
    print()


'''
def asterisk(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

asterisk('1', '2', '3', forth='helen', fifth='tom')
'''