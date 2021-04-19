import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    patterns = input()
    test = ''   # 비교할 str

    total = 0  # 마디의 길이
    for i in range(1, len(patterns)):
       total = i
       if patterns[:i] != patterns[i:2*i]:
            continue
       else:
           break
    print('#{} {}'.format(tc, total))
