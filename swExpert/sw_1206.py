"""
lv3
flag - 좌우 2칸 이내에 건물이 같거나  큰게 있으면 바로 for문을 빠져 나옴으로써 성능 개선
"""
move = [-2, -1, 1, 2]
# 테스트 케이스는 10개이다.
for t in range(10):
    N = int(input())
    buildings = list(map(int, input().split()))
    cnt = 0

    for i in range(2,N-2): # 양쪽 두 칸은 빌딩이 지어지지 않는다.
        flag = True
        for k in move:
            if buildings[i+k] >= buildings[i]:
                flag = False # 해당 빌딩은 조망권을 보장 받지 못한다.
                break
        # 위 4가지 move형태에서 조건에 해당하지 않는다면 조망권이 보장된것이다.
        if flag == True:
            # 좌우 2칸 이내의 빌딩 중에 제일 높은 빌딩이 기준이 된다.
            cnt += (buildings[i] - max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2]))
    # 해당 테스트 케이스에 대한 결과 출력
    print(f'#{t+1} {cnt}')
