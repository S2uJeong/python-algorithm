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