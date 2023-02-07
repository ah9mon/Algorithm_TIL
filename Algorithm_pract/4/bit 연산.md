# 비트연산으로 부분집합 구하기

## 준비물

```python
arr = ['fish', 'and', 'chips']
N = len(arr)

# arr에 대한 모든 경우의 수
for i in range(1 << N):
    # j : arr의 index
    for j in range(N):
        if i & (1 << j):
            print(arr[j], end = ' ')
    print()
```

## 실행결과

```python
fish
and
fish and
chips
fish chips
and chips
fish and chips
```

## `1 << 2 ` 의 의미

```python
N = 3

print(1 << N) # 8
```

- `<<` 피연산자를 비트열에서 왼쪽으로 이동시킨다. 

| 2진수  | 10진수 | shift횟수 |
| ---- | ---- | ------- |
| 0001 | 1    | 0       |
| 0010 | 2    | 1       |
| 0100 | 4    | 2       |
| 1000 | 8    | 3       |

- `for i in range(1 << N):` 
  
  - `for i in range(8)`
  
  - 3개의 원소를 가지고 우리가 만들 수 있는 모든 경우의 수는 8(2^3)개 

`arr = ['fish', 'and', 'chips']` 의 각 요소를 비트로 나타내보자.

- 1번째, 2번째, 3번째 요소에 해당한다.
  
  - arr의 index를 경우의 수에 따라 부분집합에 포함을 시킬 것이냐 시키지 않을 것이냐 

| fish | and | chips |
| ---- | --- | ----- |
| 001  | 010 | 100   |

# `if i & (1 << j)`이해하기

비트연산자 &(and) 두 비교 대상의 비트 값의 각 자리수를 비교한다.

양쪽의 자리수가 모두 True(1) 일때 True를 반환한다.

- 숫자 3(N)을 받고 i(3)번째 경우의 수 
  
  `3 & (1<<0)` -> True
  
  | 3      | 0   | 1   | 1   |
  | ------ | --- | --- | --- |
  | fish   | 0   | 0   | 1   |
  | result | 0   | 0   | 1   |
  
  `3 & (1<<1)` -> True
  
  | 3      | 0   | 1   | 1   |
  | ------ | --- | --- | --- |
  | and    | 0   | 1   | 0   |
  | result | 0   | 1   | 0   |
  
  `3 & (1<<2)` -> False
  
  | 3      | 0   | 1   | 1   |
  | ------ | --- | --- | --- |
  | chips  | 1   | 0   | 0   |
  | result | 0   | 0   | 0   |

- 즉, 배열 `arr = ['fish', 'and', 'chips']`의 부분집합의 경우의 수 중,

- 3번째 경우는 `fish, and` 두 요소를 포함한 것과 같다.
