# mid : 두 말의 거리
# 조건 : 주어진 마리 만큼의 말이 마굿간에 다 들어가야함 not over max(dist)

Space, Horse = map(int,input().split())
dists = [int(input()) for _ in range(Space)]
dists.sort()

lt, rt = 1, dists[-1]
res = dists[-1]
print(f'최대 좌표 : {dists[-1]}')
while lt <= rt :
    crtX = dists[0]
    cnt = 1  # 현재 말의 위치 및 위치 된 말은 다 1로 시작한다.
    mid = (lt+rt)//2
    print(f'mid = {mid}, crtX = {crtX}, cnt = {cnt}')
    for idx, dist in enumerate(dists):
        if dist - crtX  >= mid :
            cnt += 1
            crtX = dist #crtX += dist
        print(f'crtX = {crtX}, cnt = {cnt}')
    print(f'lt,rt 바뀌기 전 최종 cnt : {cnt}')
    if cnt >= Horse:
        cnt = 0
        lt = mid + 1
        res = mid
    else :
        cnt = 0
        rt = mid - 1
    print(f'lt = {lt}, rt = {rt}')

print(res)