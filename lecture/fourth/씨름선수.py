N = int(input())
infos = [list(map(int,input().split())) for _ in range(N)]
res = 0

infos.sort(key = lambda x : -x[0]) # 키로 정렬한다.(내림차순)
print(f'sorted_list : {infos}')
# 아이디어 : 키로 이미 정렬되었으니, for문을 돌 때, i번째 선수는 이미 그 이전 번호의 선수들 보단 작으므로
#        몸무게라도 이전 선수들 중에서 제일 커야 한다.
max_w  = -1
for h,w in infos:
    if w >= max_w:
        max_w = w
        res += 1

print(res)


