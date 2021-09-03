# 1. 입력 받기
while True:
    s, e = map(int, input().split())
    # 1-1. 입력 범위를 벗어나면 다시 받기
    if s < 2 or e < 2 or s > 9 or e > 9:
        print("INPUT ERROR!")
    else:
        break

# 2-1. start bigger than end number
if s > e:
    for i in range(1, 10):
        for j in range(s, e-1, -1):
            print(f'{j} * {i} = {j * i:>2}', end='   ')
        print()
else:
    for i in range(1, 10):
        for j in range(s, e+1):
            print(f'{j} * {i} = {j * i:>2}', end='   ')
        print()
