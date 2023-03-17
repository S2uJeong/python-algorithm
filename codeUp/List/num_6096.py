answerList = [0]*19

# 바둑판 입력 받기
for i in range(19):
    answerList[i] = list(map(int,input().split()))
# 놓을 바둑알 갯수
num = int(input())

for i in range(num):
    x,y = map(int,input().split())

    for j in range(19):
        if answerList[x-1][j] == 0:
            answerList[x-1][j]= 1
        else : answerList[x-1][j] = 0
        if answerList[j][y-1] == 0:
            answerList[j][y-1] = 1
        else:
            answerList[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(answerList[i][j], end=" ")
    print()