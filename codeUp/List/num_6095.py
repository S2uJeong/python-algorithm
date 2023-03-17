# 이차원 배열(list) 사용하는 방법
answerList = [];
for i in range(20):
    answerList.append([])  # 리스트 안에 아무것도 없는 빈 리스트 만들기
    for j in range(20):
        answerList[i].append(0) # 0으로 채우기

num = int(input())

for i in range(num):
    x, y = input().split()
    answerList[int(x)][int(y)] = 1

for i in range(1,20):
    for j in range(1,20):
        print(answerList[i][j], end=' ') # 공백을 두고 한 줄로 출력한다.
    print() # 줄 바꿈

