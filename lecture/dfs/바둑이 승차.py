w, n = map(int,input().split())
weights = [int(input()) for _ in range(n)]
max_w = -(1e10)
total = sum(weights)
def DFS(L,sum, tsum):
    global max_w
    # 가지치기
    if sum + (total - tsum) < max_w :
        return
    # 조건 맞추기
    if sum > w :
        return
    if L == n :
        if sum > max_w:
            max_w = sum
    else:
        DFS(L+1, sum, tsum+weights[L])
        DFS(L + 1, sum+weights[L] , tsum+weights[L]) # L인덱스의 강아지 무게를 포함한다.
# main
DFS(0,0,0)
print(max_w)