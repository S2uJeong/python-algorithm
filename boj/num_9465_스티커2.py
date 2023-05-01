for i in range(int(input())):
    n = int(input())
    stikers = [[0] + [*map(int, input().split())] for _ in range(2)]

    for i in range(2,n+1):
        stikers[0][i] += max(stikers[1][i-2:i])
        stikers[1][i] += max(stikers[0][i-2:i])
    print(max(stikers[0][-1], stikers[1][-1]))