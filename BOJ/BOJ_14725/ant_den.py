# 먹이 정보 개수만큼
arr = []
for i in range(int(input())):
    temp = list(input().split())
    # '--' 붙여주기
    temp = temp[1:]
    for j in range(len(temp)):
        temp[j] = '--'*j + temp[j]

    arr.append(temp)

# 1. 사전 순서로 정렬
arr.sort()

# 결과값 저장할 변수
result = arr[0]

for i in range(len(arr) - 1):
    before = arr[i]
    after = arr[i + 1]
    for j in range(len(after)):
        # 2. j가 before의 원소의 개수보다 크면 추가
        if j > len(before):
            result.append(after[j])

        else:
            # 같지 않으면(여기서부터 다) 추가해줘야 함
            if before[j] != after[j]:
                for k in range(j, len(after)):
                    result.append(after[k])
                break

for i in range(len(result)):
    print(result[i])

