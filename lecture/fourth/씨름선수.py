N = int(input())
infos = [list(map(int,input().split())) for _ in range(N)]
res = 0

infos.sort(key = lambda x : -x[0]) # 키로 정렬한다.(내림차순)
print(f'sorted_list : {infos}')
# 아이디어 : 키로 이미 정렬되었으니, for문을 돌 때, i번째 선수는 이미 그 이전 번호의 선수들 보단 작으므로
#        몸무게라도 이전 선수들 중에서 제일 커야 한다.
for idx, val in enumerate(infos):
    # 현재 기준이 되는 학생의 키와 몸무게
    tmp_h = val[0]
    tmp_w = val[1]
    print(f'현재 선수 위치 : {idx}')
    # 이전 선수들하고만 몸무게를 비교한다.
    tmp_max_w = -1
    for j in range(0,idx):
        if infos[j][1] > tmp_max_w:
            tmp_max_w = infos[j][1]
    if tmp_w >= tmp_max_w:
        res+=1
    print(f'무게 : {tmp_w} vs 이전 선수들 중 최대 무게 : {tmp_max_w} ------res : {res}')

print(res)


