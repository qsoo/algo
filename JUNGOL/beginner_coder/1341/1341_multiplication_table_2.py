s, e = map(int, input().split())
epoch = 1
if s > e: epoch = -1

for i in range(s, e + (epoch), epoch):
    for j in range(1, 10):
        print(f'{i} * {j} = {i * j:>2}', end ='   ')
        if not (j % 3):
            print()
    print()