"""
https://www.acmicpc.net/problem/20366

눈덩이 중 4개를 골라 눈사람을 2개 만드는데, 이 두 눈사람의 길이 차이가 최소값을 구하라
눈덩이 : 4 ~ 600
눈덩이 지름 : 1 ~ 1e9

이차원 배열(600*600)을 만들어서, i번째와 j번째 눈덩이를 조합했을 때 길이를 저장해 놓고 이차원 배열을 돌며 비교한다.
  1. i == j 면 안됨
  2. (i,j)을 기준으로 탐색 시, i행과 j열은 제외하고 탐색해야함. 눈덩이를 중복해서 쓸 수 없음
"""
import sys
input = sys.stdin.readline

N = int(input().rstrip())
snows = list(map(int,input().split()))

snowmans = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        snowmans[i][j] = snows[i] + snows[j]

print(snowmans)
result = int(2e10)
i = 0
j = 1
while i < N :
    for r in range(N):
        if r == i :
            continue
        for c in range(N):
            if r == c or c == j:
                continue
            result = min(result, abs(snowmans[i][j] - snowmans[r][c]))
            print(result)

    j += 1
    if j == i:
        j += 1
    if j >= N :
        i += 1
        j = 0



print(result)