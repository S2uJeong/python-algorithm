while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0 :
        break

    matrix = [list(map(int,input().split())) for _ in range(N)]
    memo = [[0] * (M+1) for _ in range(N+1)]

    result = 0
    # dp활용해서 memo update
    for r in range(1,N+1):
        for c in range(1,M+1):
            if matrix[r-1][c-1]:
                memo[r][c] = min(memo[r-1][c], memo[r-1][c-1], memo[r][c-1]) + 1
                result = max(memo[r][c], result)

    print(result)