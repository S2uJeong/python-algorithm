import sys
input = sys.stdin.readline
N,M = map(int,(input().split()))
times = list(map(int,input().split()))

def check(mid):
    cnt = 0
    for time in times:
        cnt += (mid // time)
    return cnt >= M

lo, hi = 0, min(times) * M
while lo+1 < hi : # lo와 hi 가운데 mid가 생길 수 있는 조건문
    mid = (lo + hi) // 2
    if check(mid):
        hi = mid
    else :
        lo = mid

print(hi)
