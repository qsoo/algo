## 1953. 탈주범 검거

[문제 링크](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq)

1회독: 20.11.03



### Idea

Input data를 받는 방식에 따라 문제 난이도가 달라지기 때문에 리스트에 문자열이 담긴 형태로 처리 

(1) 삽입 작업을 할 때 insert 함수를 사용하게 되면 

뒤로 쌓이는 형태가 되지 않기 때문에 이 부분을 처리해줘야 함 

(2) 삽입, 삭제, 추가 각 작업의 조건 분기를 만들어 준 다음 인덱스를 사용해서 암호문을 조작 

(3) 제거에는 pop을 이용해서 작업 시행



### my solution

```python
for tc in range(1, 11):
    N = int(input())
    # 원본 암호문
    crypto = list(map(str, input().split()))
    # 명령어 개수
    K = int(input())
    statement = list(map(str, input().split()))

    # 1. while문으로 탐색을 한다 i - idx로 사용할 것
    i = 0

    while i < len(statement):
        # 1. 삽입 작업 수행
        if statement[i] == 'I':
            # 삽입할 인덱스의 위치를 담는다
            insert_idx = int(statement[i + 1])
            # j == 삽입할 개수 => int 자료형 변환
            j = int(statement[i + 2])
            # 첫번째 나오는 원소를 해당 위치에 넣는다 
            # => 전체를 넣어버리면 앞으로 계속 들어옴
            crypto.insert(insert_idx, statement[i + 3])
            # 위에서 원소 하나는 넣었다!
            i = i + 4
            # insert 작업 한번 해줬기 때문에 끝 지점 index(문자앞 값)는 -1을 해줘야 함
            endpoint = i + j - 1
            # insert 작업 동안 index로 사용할 값
            k = 1
            # 삽입 작업 수행
            while i < endpoint:
                # 해당 위치에 들어간 다음에는 뒤에 들어가야 함
                crypto.insert(insert_idx + k, statement[i])
                i += 1
                k += 1
                
        # 2. 삭제 작업 수행
        elif statement[i] == 'D':
            # 삭제할 index
            delete_idx = int(statement[i + 1])
            # 삭제할 총 개수
            j = int(statement[i + 2])
            # 그 다음 수행작업(문자) 오는 index로 증가
            i = i + 3
            # pop 작업 반복
            while j:
                result = crypto.pop(delete_idx)
                j -= 1

        # 3. append 작업 수행
        elif statement[i] == 'A':
            # 추가할 개수 저장
            j = int(statement[i + 1])
            # 추가할 값들 있는 index로 i 이동시키기
            i = i + 2
            # 끝 지점 == 새로운 수행작업(문자)가 들어오는 지점
            endpoint = i + j
            while i < endpoint:
                crypto.append(statement[i])
                i += 1
    # 출력
    print('#{} {}'.format(tc, ' '.join(crypto[:10])))
```



### 태그

- 리스트
- while