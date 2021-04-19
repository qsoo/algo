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