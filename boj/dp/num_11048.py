"""
이동 방향이 정해져 있고, 미로 밖을 나가선 안됨, 도착지는 (N,M)
칸을 방문하면 해당 값만큼 사탕을 얻음
해당 사탕의 개수가 최대값이 되도록 로직 생성
"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
maps = [[0] * (M+1)] + [[0] + list(map(int,input().split())) for _ in range(N)]

for i in range(1,len(maps)):
    for j in range(1,len(maps[0])):
        maps[i][j] = max(maps[i-1][j-1], maps[i-1][j], maps[i][j-1]) + maps[i][j]

print(maps[N][M])