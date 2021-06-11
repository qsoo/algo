## 601. 문자열1 - 자가진단9

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=238&sca=10e0)

1회독: 21.06.11



### my solution

```python
str = input().strip()
length = len(str)
for i in range(1, (length + 1)):
    # 1. 오른쪽으로 밀었을 때 앞으로 오는 문자
    print(str[-i::] + str[:(length - i)])
```

python slice를 이용하여  

(1) 오른쪽으로 이동했을 때 끝지점이라 앞으로 오는 부분을 먼저 출력 

(2) 나머지는 그대로 출력



### 참고 자료

#### Python Slice 문법

- `Array[a:b:c]` 형식으로 사용 가능

  > index a 부터 index b(미만)까지 c의 간격으로 배열의 값 가져오기

- `Array[slice(a, b, c))` 형식으로도 사용 가능

- `[::]`: 리스트 전체 가져오기(deep copy)



### 태그

- 문자열
- slice 문법

