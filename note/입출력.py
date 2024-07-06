# 리스트 만들기
memo = [0] * 10 # 최대 9층까지 있다.
memo2 = [[0] for _ in range(10)]
print(memo)
print(memo2)
## 결과
memo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
memo2 = [[0], [0], [0], [0], [0], [0], [0], [0], [0], [0]]

# =======================================================

# 정수형 자료, 한 줄에 띄어쓰기로 구분된 입력, 리스트로
## 1 2 3 4 5
input = list(map(int,input().split()))
print(input)

# 정수형 자료, 한 줄에 띄어쓰기로, 각각 변수에
## 2 3 4
x,y,z = map(int,input().split())
print(x,y,z)

# readline() 활용 - 1,000만 개 넘는 라인 입력 경우
import sys
data = sys.stdin.readline().rstrip()

# print 시 자료형 혼합해서 + 연산 안됨
num = 14
print("답은 " + str(num) + " 이다.")
print("이것도 답이", str(num), "된다.") # , 가 공백으로 들어가게 함에 유의
print(f"정답은 {num} 입니다.")


# sep, 기준에 따라 입력받고 출력한다.
a, b = input().split(':')
print(a, b, sep=':')


# 연산자를 통해 str 변수를 몇번 반복해서 출력가능
print("string"*3)
# 결과 : stringstringstring

# 유니코드
int_value = ord(input())
char_value = chr(input())