'''
# T: 탐색을 실시할 문자열(in) - text
T = input()
# P: 탐색을 할 문자열(target) - pattern
P = input()
'''
T = 'ABC ABCDAB ABCDABCDABDE'
P = 'ABCDABD'


def boyer_moore(T, P):

    n, m= len(T), len(P)

    # start point 지정
    k = 0

    # 결과값 저장
    cnt = 0
    result = []

    # index 범위 안 벗어나는 동안
    while k <= n - m:
        # 패턴 있는지 확인할 변수
        is_contained = True
        # 1. 뒤 부터 탐색해서 맞는지 확인
        i = m - 1
        while i >= 0:
            # 2. 하나씩 비교
            if P[i] != T[i + k]:
                is_contained = False
                # 3. 다를 때의 P의 문자열이 T 안에 있는지 판단
                movepoint = check_idx(P, T[i + k])
                break
            i -= 1

        if i == -1:
            cnt += 1
            result.append(k)

        else:
            k += movepoint

    return cnt, result

def check_idx(P, text):
    for i in range(len(P) - 1, -1, -1):
        if P[i] == text:
            return len(P) - i - 1

    return len(P)


cnt, result = boyer_moore(T, P)

print(cnt)
print(*result)
