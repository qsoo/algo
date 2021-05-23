## 551. 반복제어문3 - 자가진단4

[문제 링크](http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=188&sca=1080)

1회독: 20.12.15



### Idea

문자열을 왼쪽에는 공백을 두고 오른쪽에 출력하기

[참고자료](https://blackhippo.tistory.com/entry/Python-print%EB%AC%B8-%EC%98%A4%EB%A5%B8%EC%AA%BD%EC%99%BC%EC%AA%BD-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-%EC%9D%80%ED%96%89%EB%B2%88%ED%98%B8%ED%91%9C-%ED%91%9C%ED%98%84%ED%95%98%EA%B8%B0)



### my solution

```python
n = int(input())
for i in range(n, 0, -1):
    print(('*'*i).rjust(n))
```

참고

```python
# str.rjust(width[, fillchar])
width의 길이에 부족하면 왼쪽은 공백을 두겠다

# str.ljust() / str.center() 존재

# example
print('123'.rjust(5))
=> '  123'
```



### 태그

- 문자열 정렬
- 출력