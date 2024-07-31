"""
방법 1. combi_third_for_method : 조합을 구해서 총 무게를 확인하고 가치를 비교한다. => 시간초과
방법 2. knapsack

이차원 배열 dp
dp[N][K] 근거 : 1부터 N개의 모든 물건들을 살펴보고, 배낭 용량이 K일 때 배낭의 가치를 구해야 하므로
dp[i][j] : 처음부터 i번째까지의 물건을 살펴보고, 배낭의 용량이 j였을 때 배낭에 들어간 물건의 가치합의 최대값
dp[i][j] = max( dp[i-1][j], dp[i-1][j-w[i]] + v[i] )
                i번째 물건 안 넣는다.    i번째 물건 넣는다.
일차원 배열 dp
"""
from itertools import combinations

def combi_third_for_method(N,K,items):
    max_value = -(1e9)
    items_idx = [i for i in range(N)]

    for i in range(N):
        for combi in combinations(items_idx, i):
            w_sum = 0
            v_sum = 0
            for idx in combi:
                w_sum += items[idx][0]
                v_sum += items[idx][1]
            if w_sum <= K and v_sum > max_value:
                max_value = v_sum

    return max_value


def knapsack(K, items):
    # dp 배열 초기화
    dp = [0] * (K + 1)

    for w,v in items:
        for j in range(K, 0, -1):
            if w <= j:
                dp[j] = max(dp[j], dp[j - w] + v)

    return dp[K]

N, K = map(int, input().split())
items = [list(map(int,input().split())) for _ in range(N)]

print(knapsack(N,K,items))