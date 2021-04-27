## Quick Sort

- 정렬



- Quick Sort로 정렬한 array를 반환하는 Short Coding

  ```python
  def quick_sort(collection: list) -> list:
  
      # 종료 조건
      if len(collection) < 2:
          return collection
  
      pivot = collection.pop()
      greater = []
      lesser = []
      for element in collection:
          (greater if element > pivot else lesser).append(element)
  
      return quick_sort(lesser) + [pivot] + quick_sort(greater)
  
  
  for tc in range(1, int(input()) + 1):
      N = int(input())
      arr = list(map(int, input().split()))
  
      result = quick_sort(arr)
  
      print('#{} {}'.format(tc, result[N//2]))
  ```

  