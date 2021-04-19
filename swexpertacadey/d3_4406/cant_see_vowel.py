for tc in range(1, int(input()) + 1):
    # 모음 사전 리스트 생성
    vowel = ['a', 'e', 'i', 'o', 'u']

    sentence = input()
    result = ''
    for word in sentence:
        if word in vowel:
            continue
        else:
            result += word

    print('#{} {}'.format(tc, result))

'''
3
congratulation
synthetic
fluid
'''