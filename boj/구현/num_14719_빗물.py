n, m = map(int,input().split())
drops = list(map(int,input().split()))
answer = 0
for i in range(1,m-1):
    left_max = max(drops[:i])  # 현 위치 제외한 왼쪽 다
    right_max = max(drops[i+1:])

    if drops[i] < left_max and drops[i] < right_max:
        answer = answer + min(left_max,right_max) - drops[i]

print(answer)
