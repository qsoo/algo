import sys
sys.stdin = open('1215.txt', 'r')

def check_palindrome_col(y, x):
    global result

    col_palindrome = ''
    for i in range(y, y + target):
        col_palindrome += arr[i][x]

    endpoint = target // 2

    # col 검사
    i = 0
    while i < endpoint:
        # idea - 왼쪽 끝과 오른쪽 끝을 비교한다
        if col_palindrome[i] == col_palindrome[-(i + 1)]:
            is_palindrome_col = True
        else:
            is_palindrome_col = False
            break
        i += 1

    if is_palindrome_col:

        result += 1


def check_palindrome_row(y, x):

    global result
    # 가로, 세로 탐색
    row_palindrome = arr[y][x:x+target]

    # 회문여부 검사하는 문장의 가운데에 오게 되면 종료
    endpoint = target // 2

    i = 0
    while i < endpoint:
        # row 검사
        if row_palindrome[i] == row_palindrome[-(i + 1)]:
            is_palindrome_row = True
        else:
            is_palindrome_row = False
            break
        i += 1

    if is_palindrome_row:

        result += 1


for tc in range(1, 11):
    # target: 찾아야하는 회문의 길이
    target = int(input())
    arr = [input() for _ in range(8)]

    # 2. 가져온 배열이 회문인지 판별
    # 3. 세로에서도 반복

    result = 0
    # 1. 타겟의 길이만큼 배열에서 가져오기 - 행, 열 나눠서
    for y in range(8):
        for x in range(8 - target + 1):
            check_palindrome_row(y, x)

    for y in range(8 - target + 1):
        for x in range(8):
            check_palindrome_col(y, x)

    print('#{} {}'.format(tc, result))