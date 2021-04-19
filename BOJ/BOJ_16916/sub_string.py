# S: 탐색 대상 문자열, P: 부분 문자열?
S = input()
P = input()


# 2. 부분문자열 여부 판단
def check_sub(i:int) -> int:
    global is_sub

    if S[i:i + len(P)] == P:
        is_sub = 1
        return


# 1. 부분문자열 start와 같은 부분 탐색
is_sub = 0


# 1-1. 길이가 같은 경우 걸러주기
if len(S) == len(P):
    check_sub(0)

else:
    for i in range(len(S) - len(P)):
        if S[i] == P[0]:
            check_sub(i)
            if is_sub:
                break

print(is_sub)