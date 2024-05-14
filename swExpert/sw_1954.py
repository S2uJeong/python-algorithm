T = int(input())
for test in range(T): # 테스트케이스 개수 만큼 반복한다.
    N = int(input()) # 정사각형 한 변의 크기
    move = [(0,1),(1,0),(0,-1),(-1,0)] # 우, 하, 좌, 상 순서 (달팽이 집 생김새)
    result = [[0] * N for _ in range(N)]
    r,c = 0, 0
    dist = 0

    for n in range(1,N*N+1): # 그려질 숫자를 기준으로 for문
        result[r][c] = n
        r += move[dist][0]
        c += move[dist][1]
        # 범위를 벗어나거나 다른 값이 이미 있으면 방향 바꾸기
        if r < 0 or r >= N or c < 0 or c >= N or result[r][c] != 0 :
            # 나아가기 취소
            r -= move[dist][0]
            c -= move[dist][1]
            # 방향 전환
            dist = (dist+1) % 4
            # 방향 전환한 대로 전진
            r += move[dist][0]
            c += move[dist][1]

    print(f'#{test+1}')
    for list in result:
        for x in list :
            print(x, end=' ')
        print()

