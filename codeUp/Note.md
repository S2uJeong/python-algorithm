> range 함수는 iterable한 객체로 감싸줘서 출력할 수 있다.

```
print(range(5)) 
print(list(range(5)))  

# 출력값
range(0, 5)
[0, 1, 2, 3, 4]
```


> 공백을 기준으로 한번에 두가지 값을 input 받을 수 있다.
``` 
a,b = input().split()
a = int(a)
b = int(b)
print(a)
print(b)

# 출력값
1 2
1
2
```

>print문 안에 쉼표(,)를 넣으면  공백이 된다.
```
print(a,b) 
>>> a b
```

>sep, 기준에 따라 입력받고 출력한다.
```
a, b = input().split(':')
print(a, b, sep=':')

a:b
>>> a:b
```

>입력 받은 정수 더하는 방법 

🔴 input()으로 입력되는 값은 기본적으로 문자열로 인식된다.
```
# 의도한 대로 나오는 코드 
a,b = input().split();
c = int(a) + int(b)
print(c);

# 입력된 값이 숫자여도 문자로 인식되어 문자가 합쳐진 값이 나옴
a,b = input().split();
c = a + b;
print(c);

# 문자로 합쳐진 걸 int화 하려고 해서 오류남 
a,b = input().split();
c = int(a + b);
print(c);
```

>진수변환
```
a = input();
n = int(a)    # 정수를 
print('%x'%n)  # 16진수로 hexadecimal 대문자로 출력 : '%X'
print('%o'%n)  # 8진수로  octal

a = inout();
n = int(a,16) # a를 16진수로 인식해 변수 n에 저장
print('%o'%n) # 16진수를 8진수 문자열로 출력 
```

>유니코드
```
# 문자 -> 정수값
n = ord(input())
# 정수 -> 문자
a = input()
n = chr(a) 
```

>정수 변환
- 단항 연산자인 `-` 를 변수 앞에 붙이면 부호가 반대인 값이 된다.
```
print(-n)
```

>String 출력의 다양성
```
1. * 연산자를 통해 str 변수를 몇번 반복해서 출력가능
>>> print(string*3) 
stringstringstring
```
>List 관련 함수

- map
  - string은 한 요소씩 쪼개고 싶으면 `변수명[int]`를 이용하여 손 쉽게 나눌 수 있따
  - 하지만 int형 변수의 값은 위의 방식으로 나눌 수 없다. 그래서 사용하는 것이 map이다.

  - 리스트의 요소를 지정된 함수로 처리해주는 함수
  - 원본 리스트를 변경하지 않고 새 리스트를 생성한다.
  ```
  list(map(함수, 리스트))
  tuple(map(함수, 튜플))
  ```
- min
  - list 안에서 최소값을 반환하는 함수  
    ```
    min = min(list);
    ```
    
>2차원 List 만들기
...
d=[]
for i in range(20) : 
  d.append([])
  for j in range(20) :  
    d[i].append(0)
... 

>여러가지 정리
1. sorted() 함수는 O(NlogN)을 보장하며 튜플을 sorted()해도 리스트 자료형으로 반환한다.
2. 리스트를 정렬할때는 리스트명.sort()로 바로 정렬 가능.

### 자료구조
- 스택
  - 별도의 라이브러리가 필요없다.
  - 기본 리스트에서 append(), pop() 메서드를 이용하면 스택 자료구조와 동일하게 동작

- 큐
  - 구현을 위해 deque 라이브러리를 사용한다. 
  ```
  from collections import deque # 라이브러리 호출
  queue = deque()
  queue.append(1)
  queue.append(5)
  queue.popleft() # 1이 삭제
  ```
  - .reverse()
  - list() 메서드를 이용하면 큐를 리스트 자료형으로 변환 가능하다. 

### 에러로그
```
IndexError: list assignment index out of range
```
- 빈 리스트에 인덱스를 지정해서 나온 에러이다. 
- (19*19) 2차원 자료구조를 만들기 위하여 아래와 같이 코드를 짰는데 해당 에러가 발생하였다.
```
list = []

for i in range(19):
    answerList[i] = list(map(int,input().split()))
```
- 해결방법은, 원하는 열 갯수만큼 먼저 초기화를 하는 것이다.
```
answerList = [0]*19

for i in range(19):
    answerList[i] = list(map(int,input().split()))
```