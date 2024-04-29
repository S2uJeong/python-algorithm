"""
1. 갭의 중앙값으로 시작해 이진탐색으로 가장 인접한 두 공유기 사이의 거리(gap)을 조절해가며,
2. 매 순간 실제로 공유기를 설치하여 C보다 많은 개수로 공유기를 설치할 수 있는지 체크
3. 체크 시, 더 많은 개수로 넘어가는 순간 설치를 못한다면, 그 바로 직전 값이 정답
"""
N, C = map(int,input().split())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()

start = 1 # 가능한 최소 거리
end = data[-1] - data[0] # 가능한 최대 거리
result = 0

while(start <= end):
    mid = (start+end) // 2
    value = data[0]
    count = 1
    # 현재의 mid 값을 이용해 공유기를 설치
    for i in range(1,N):
        if data[i] >= value + mid :
            value = data[i]
            count += 1
    if count >= C :
        start = mid +1
        result = mid
    else :
        end = mid -1

print(result)