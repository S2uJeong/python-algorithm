import sys

input = sys.stdin.readline

m, n = map(int, input().split())
heights = list(map(int, input().split()))

# 기준이 될 왼쪽 벽 정하기 
start_point = 0
for i in range(len(heights)):
    if heights[i] != 0:
        start_point = i
        break

    # 기준이 될 오른쪽 벽 정하기
end_point = 0
for i in range(len(heights) - 1, -1, -1):
    if heights[i] != 0:
        end_point = i
        break

answer = 0
for i in range(start_point + 1, end_point):  # 왼쪽벽과 오른쪽벽은 제외하고서 계산.
    l_max = max(heights[:i])
    r_max = max(heights[i+1:])
    #print(f'r_max = {r_max}, l_max = {l_max}')

    if min(l_max, r_max) > heights[i]:
        answer += min(l_max, r_max) - heights[i]
    #print(f'{i}번째 일때 answer + {min(l_max, r_max) - heights[i]} = {answer}')
print(answer)