import sys
input = sys.stdin.readline

N, target = map(int, input().split())
trees = list(map(int, input().split()))

def check(mid):
    sum = 0
    for tree in trees:
    #    sum += max(tree-mid, 0)
        if tree >= mid :
            sum += (tree-mid)
    return sum >= target

# 절단기의 높이
lo = 0
hi = max(trees) # 절단기의 높이는 제일 큰 나무 길이를 초과하면 의미가 없다. (제일 큰 나무 높이 시, 이미 절단이 0으로 정해짐)

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if check(mid):
        lo = mid  # 절단기의 높이를 높여라 (절단기 높이가 낮을 수록 T)
    else:
        hi = mid

print(lo)