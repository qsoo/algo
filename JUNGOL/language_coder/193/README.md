## 193. 문자열2 - 형성평가5

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=93&sca=10f0)

1회독: 21.06.22



### my solution

```python
i = 0
arr = []
while i < 5:
    i += 1
    arr.append(input().strip())

target = []
for _ in range(2):
    target.append(input().strip())

is_catch = False

for i in arr:
    for j in target:
        if j in i:
            print(i)
            is_catch = True
            break

if not is_catch:
    print("none")
```

(1) 5개의 대상 단어 while 문으로 입력 받아서 리스트 내에 저장

(2) 포함된 단어(찾을 단어)는 target 리스트에 저장

(3) python은 간단하게 `in` 구문으로 포함 여부 확인 가능

(단, 'tomato'에서 'o'와 'ma'를 찾게 되면 두 번 나오게 되기 때문에 break 문으로 반복문 나가주기)

(4) 못 찾을 때의 flag 설정해서 조건에 맞게 출력

 

### 태그

- 문자열
- 반복문
- 입력