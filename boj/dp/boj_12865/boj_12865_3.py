"""
물건 n개, 최대 K만큼의 무게를 넣는 배낭 1개

물건의 조합을 구해 가치의 최대 값을 찾을 수 있겠지만, 물건이 최대 100개이므로 100 * 99 * ... * 1 의 복잡도가 걸리는 조합법은 시간복잡도를 충족하지 못한다.
DP를 통해 가방에 있는 물품의 무게를 늘리며 그 무게만큼 가질 수 있는 가치의 최대 값을 매번 갱신하며 전개한다.

중복 문제가 발생하지 않도록 역방향을 순회하는 것에 주의한다.
*정방향 순회 문제 시뮬레이션:
1. 초기 상태: dp = [0, 0, 0, 0, 0, 0].
2. (2, 3) 처리:
    cur_w = 2: dp[2] = max(dp[2], dp[0] + 3) = 3.
    cur_w = 3: dp[3] = max(dp[3], dp[1] + 3) = 3.
    cur_w = 4: dp[4] = max(dp[4], dp[2] + 3) = 6. (문제 발생).
"""
N, MAX_WEIGHT = map(int,input().split())
product_info = []
for _ in range(N):
    product_info.append(list(map(int,input().split()))) # 무게, 가치

dp = [0] * (MAX_WEIGHT+1)

# 시간 복잡도 : 이중 for문 100_000 * 100 = 10_000_000
for w, v in product_info:
    for cur_w in range(MAX_WEIGHT, w - 1, -1):  # 역방향으로 순회
        dp[cur_w] = max(dp[cur_w], dp[cur_w - w] + v)

print(dp[MAX_WEIGHT])
