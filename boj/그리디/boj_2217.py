"""
1. 각 로프의 최대 중량을 내림차순으로 정렬한다.
2. "최대 중량" 이므로 기준은 병렬로 설치될 로프 중 제일 작은 중량을 드는 로프에 맞춰 최대 중량을 계산한다.
"""
N = int(input())
ropes = [int(input()) for _ in range(N)]
ropes.sort(reverse=True)

result = 0
for i in range(len(ropes)):
    result = max(result, ropes[i] * (i+1))

print(result)