import sys

T = int(input())

for i in range(T):
    n = int(input())
    arrScore = []

    # 점수 입력받기
    for column in range(2):
        arrScore.append(list(map(int,sys.stdin.readline().split())))

    for row in range(1,n):
        if row == 1:
            arrScore[0][row] += arrScore[1][row-1]
            arrScore[1][row] += arrScore[0][row-1]
        else:
            arrScore[0][row] += max(arrScore[1][row-1],arrScore[1][row-2])
            arrScore[1][row] += max(arrScore[0][row-1], arrScore[0][row - 2])

    print(max(arrScore[0][n-1], arrScore[1][n-1]))



'''
print("arrScore[0] : ")
print(*arrScore[0])
print("arrScore[1] : ")
print(*arrScore[1])
'''