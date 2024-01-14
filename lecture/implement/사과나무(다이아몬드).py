N = int(input())
mylist = [list(map(int,input().split())) for _ in range(N)]

s = e = N//2
res = 0
for i in range(N):
    for j in range(s,e+1):
        res += mylist[i][j]
    if i < N//2 :
        s -= 1
        e += 1
    else :
        s += 1
        e -= 1

print(res)