T = int(input())

for tc in range(1, T + 1):
    case_length = int(input())  # 숫자 개수
    case = list(map(int, input().split()))

    # 버블 정렬 사용
    for i in range(len(case) - 1, 0, -1):
        for j in range(0, i):
            if case[j] > case[j + 1]:
                case[j], case[j + 1] = case[j+1], case[j]

    # list 요소들 int형이기 때문에 join 불가 => 형변환 필요
    print('#{} {}'.format(tc, ' '.join(map(str, case))))