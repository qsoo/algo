# N: 총 단어의 개수
N = int(input())
arr = list(input() for _ in range(N))
# 비교를 위해 변환한 단어 담을 리스트
pair_li = []

for i in range(N):  # 100
    # 해당 단어에서 나오는 음절 저장 리스트
    temp = []
    feature = 1
    number = 0
    for j in range(len(arr[i])):    # 50
        target = arr[i][j]

        if target in temp:
            number = number * 10 + temp.index(target)

        else:
            temp.append(target)
            feature += 1
            number = number * 10 + feature

    # 2. 이를 비교 리스트에 저장
    pair_li.append(number)

# print(pair_li)

# 3. 같은 쌍이 몇개 있는지 확인
result = 0
# comb(100, 2) = 약 9900/2
for i in range(N-1):
    for j in range(i+1, N):
        if pair_li[i] == pair_li[j]:
            result += 1

print(result)