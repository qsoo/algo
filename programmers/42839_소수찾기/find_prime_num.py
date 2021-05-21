def permutation(arr, r, result):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]



    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            # shallow copy이기 때문에 이를 변수에 저장
            temp = chosen[:]
            temp = ''.join(temp)
            # 중복 제거
            if temp != '':
                temp = int(temp)
                if temp not in result:
                    result.append(temp)
            return

        for i in range(len(arr)):
            # 3.
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    return result

def check_prime(arr, count):
    for i in arr:
        target = i
        # 소수는 1보다 크다
        if 2 < target:
            for j in range(2, target):
                # 나누어 떨어지지 않는다
                if target % j == 0:
                    is_prime_number = False
                    break
                else:
                    is_prime_number = True

            if is_prime_number:
                count += 1

        elif target == 2:
            count += 1

    return count


def solution(numbers):
    count = 0
    # 순열 저장할 배열
    result = []
    for i in range(len(numbers) + 1):
        permutation(numbers, i, result)

    return check_prime(result, count)