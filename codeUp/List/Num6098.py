answer = [0]*10

for i in range(10):
    answer[i] = list(map(int, input().split()))

x,y = 1,1


while True:
    if answer[x][y] == 2:
        answer[x][y] = 9
        break
    else : answer[x][y] = 9

    if answer[x + 1][y] == 1 and answer[x][y + 1] == 1:
        break

    if answer[x][y+1] != 1:
         y += 1

    elif answer[x+1][y] != 1:
        x += 1


for i in range(10):
    for j in range(10):
        print(answer[i][j], end=" ")
    print()