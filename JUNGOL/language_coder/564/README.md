## 564. 배열2 - 자가진단1

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=201&sca=10a0)

1회독: 20.12.17



### Idea

대문자의 개수를 출력해서 보여주는 문제로 영어 대문자가 아니면 STOP 첫 아이디어는  

(1) ASCII 코드를 이용해 조건문을 만들어 주고 

(2) 딕셔너리에 key, value 쌍으로 대문자-개수를 저장해서 출력해주는 방법을 생각했으나 

현재 알파벳 사전 순으로 출력이 되어야 하기 때문에 이를 변경해주어야 했음 

따라서 영어 대문자를 담고 있는 리스트와 해당 개수를 담는 리스트 총 두개를 만들어서 

개수를 담는 리스트의 원소가 0보다 클 때만 가져와서 출력해주는 방향으로 변경



### my solution

```python
# ASCII 코드를 이용하여 입력 제한 조건 설정
start, end = 65, 90

alphabet_li = [chr(i) for i in range(start, end+1)]
alphabet_cnt = [0]*len(alphabet_li)

# 조건에 맞게 걸러주기
arr = input().split()

for i in range(len(arr)):
    # 1. 대문자인지 판별하고
    if arr[i] in alphabet_li:
        # 2. 해당 인덱스에 값 저장
        target = alphabet_li.index(arr[i])
        alphabet_cnt[target] += 1
    else:
        break

for i in range(len(alphabet_li)):
    if alphabet_cnt[i]:
        print('{} : {}'.format(alphabet_li[i], alphabet_cnt[i]))
```



### (틀린 코드)

```python
# ASCII 코드를 이용하여 입력 제한 조건 설정
start, end = 65, 90

alphabet_li = [chr(i) for i in range(start, end+1)]
result = dict()
# 조건에 맞게 걸러주기
arr = input().split()

for i in arr:
    # 1. 대문자인지 판별하고
    if i in alphabet_li:
        # 2. 현재 사전에 정의되었다면 개수를 더해주고 없다면 만들어주기
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    else:
        break

for key, val in result.items():
    print('{} : {}'.format(key, val))
```

딕셔너리를 이용하게 되면 알파벳 사전 순대로 나오지 않는 경우가 발생



### 태그

- 리스트
- 딕셔너리