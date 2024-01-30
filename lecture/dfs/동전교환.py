import sys

n = int(input())
coins = list(map(int,input().split()))
re_money = int(input())

# 동전의 단위가 큰 것을 먼저 사용할 수록 갯수가 최소가 될 확률이 높아지므로
coins.sort(reverse=True)
res = 1e10

# L(노드) : 사용한 동전의 개수
# 간선 : 어떤 동전을 사용했는지
def dfs(L,sum):
    global res
    # cut2
    if L > res :
        return
    # cut1
    if sum > re_money:
        return
    # 조건충족
    if sum == re_money:
        if L < res:
            res = L
    else :
        for coin in coins:
            dfs(L+1, sum+coin)

dfs(0,0)
print(res)
