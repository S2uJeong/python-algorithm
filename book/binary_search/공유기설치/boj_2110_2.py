import sys
input = sys.stdin.readline

N,C = map(int,input().split())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort() # 좌표가 가장 작은것 부터 순차적으로 탐색하며 결정하기 위해

start = 1# 공유기 간 최소 거리
end = data[-1] - data[0] # 공유기 간 최대 거리
result = 0
while start <= end :
    # 일단 확률이 제일 높을 중간부터 시작한다.
    mid = (start + end) // 2
    value = data[0] # 처음 시작은 제일 첫번째 집 위치
    count = 1 # 처음 위치에 놨다는 가정하에 시작
    for i in range(1,N):
        if data[i] >= value + mid:
            count += 1
            value = data[i]
    if count >= C :
        result = mid
        start = mid+1
    else :
        end = mid-1
print(result)