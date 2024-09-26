"""
가방은 한 개, 물건은 여러개 일때 정해진 무게 안에서 최대 가치를 얻는 물건을 선택하는 문제

dp[i] : 가방 안의 무게가 i 일 때, 가질 수 있는 최대 가치
"""

N, K = map(int,input().split())
things = [list(map(int,input().split())) for _ in range(N)]
dp = [0] * (K+1)

for w, v in things:
    for i in range(K, w-1, -1):  # 역순으로 처리하여 중복 선택 방지
        dp[i] = max(dp[i], dp[i-w] + v)

# for i in range(1,len(dp)):
#     for j in range(len(things)):
#         w, v = things[j]
#         if i - w >= 0 :
#             dp[i] = max(dp[i-w] + v , dp[i-1])

print(dp[K])
