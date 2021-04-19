# 20 * 20 * 2 * 20 * 20
def check_senergy(a:list, b:list):
    score_a, score_b = 0, 0

    # a팀의 총 점수 구하기
    if len(a) == 1:
        score_a = 0
    else:
        for i in range(len(a)-1):
            mate_1 = a[i]
            for j in range(i+1, len(a)):
                mate_2 = a[j]
                score_a += score[mate_1][mate_2] + score[mate_2][mate_1]

    # b팀의 총 점수 구하기
    if len(b) == 1:
        score_b = 0
    else:
        for i in range(len(b)-1):
            mate_1 = b[i]
            for j in range(i+1, len(b)):
                mate_2 = b[j]
                score_b += score[mate_1][mate_2] + score[mate_2][mate_1]

    # 최종 차이값 저장
    global result

    result = min(abs(score_a - score_b), result)
    return


def powerset(n:int, k:int):

    if n == k:
        temp_a = []
        temp_b = []
        for i in range(k):
            if visited[i] == 1:
                temp_a.append(i)
            else:
                temp_b.append(i)
        # 한 팀에 한 명이상이 있어야 한다
        if temp_a and temp_b and (temp_b, temp_a) not in all:
            # all.append((temp_a, temp_b))
            check_senergy(temp_a, temp_b)
        return

    else:
				# 포함했을 때의 경우의 부분집합 구하는 부분
        visited[n] = 1
        powerset(n+1, k)
				# 포함하지 않았을 때의 부분집합을 구하는 부분
        visited[n] = 0
        powerset(n+1, k)


# 1. N: 인원수, score: 시너지를 내는 점수
N = int(input())
# 20
score = [list(map(int, input().split())) for _ in range(N)]
# 방문여부 check 20
visited = [0 for _ in range(N)]
all = []

result = float('inf')

powerset(1, N)
# from pprint import pprint
# pprint(all)
# for i in range(len(all)):
#     check_senergy(all[i][0], all[i][1])
print(result)