w, n = map(int,input().split())
weights = [int(input()) for _ in range(n)]
max_w = 0
def DFS(L,sum):
    global max_w
    if sum > w :
        return
    if L == n :
        if sum > max_w:
            max_w = sum
    else:
        DFS(L+1, sum)
        DFS(L + 1, sum +weights[L] ) # L인덱스의 강아지 무게를 포함한다.
# main
DFS(0,0)
print(max_w)