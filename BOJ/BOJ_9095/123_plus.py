# 1. queue를 만들어서 리스트(1, 2, 3), 이전까지의 합 정보를 가져간다
# 2. N과 리스트의 합이 같아질 때 break

def one_two_three_plus(perm:list, total:int):
    global cnt
    # perm: 현재까지 저장된 배열, total: 현재까지 가지고 있는 합
    queue = []
    queue.append((perm, total))
    # iterations = 1
    while queue:
        # iterations += 1
        new_perm, new_total = queue.pop(0)
        # 1. 종료조건( == N)
        if new_total == N:
            cnt += 1
            continue
        # 2. 숫자가 초과할 때
        elif new_total > N:
            continue
        else:
            queue.append((new_perm + [3], new_total + 3))
            queue.append((new_perm + [2], new_total + 2))
            queue.append((new_perm + [1], new_total + 1))

    print(iterations)
    return

for tc in range(int(input())):
    N = int(input())
    result = []
    total = 0
    # 총 개수
    cnt = 0
    one_two_three_plus(result, total)
    print(cnt)
