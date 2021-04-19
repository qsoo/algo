from pprint import pprint
# C: column, P: 떨어지는 블록 번호
C, P = map(int, input().split())
arr = list(map(int, input().split()))

# 1. board 만들기
h = max(arr)
print(h)
board = [[0] * C for _ in range(h)]

for i in range(h):
    for j in range(C):
        if arr[j]:
            board[i][j] += 1
            arr[j] -= 1

pprint(board)

block = [0, [], [], [[0, 1, 1], [1, 1, 0]]]


def rotate(target):
    block_li = [target]
    for _ in range(3):
        target = block_li[-1]
        block = []
        for x in range(len(target[0])-1, -1, -1):
            temp = []
            for y in range(len(target)):
                temp.append(target[y][x])
            block.append(temp)
        block_li.append(block)

    return block_li


block_li = rotate(block[3])
pprint(block_li)
# # 2. 밑바닥을 체크하자
# for i in range(len(block_li)):
#     target = block_li[i]
#     print(target)
#     for k in range(C-len(target)):
#         for j in range(len(target)):
#             if target[j] == board[t]:
#                 pass
