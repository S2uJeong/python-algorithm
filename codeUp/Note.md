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
n = ord(input())
```
