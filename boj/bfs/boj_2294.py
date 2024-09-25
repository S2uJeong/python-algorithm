import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_price):
    count = 0
    visited = [False] * (K+1)
    dQ = deque([start_price])
    visited[start_price] = True
    while dQ:
        for _ in range(len(dQ)):
            cur_price = dQ.popleft()

            if cur_price == K :
                print(count)
                sys.exit(0)

            for coin in coin_info:
                next_price = cur_price + coin
                if next_price <= K and not visited[next_price]:
                    visited[next_price] = True
                    dQ.append(next_price)
        count += 1

    print(-1)

N, K = map(int, input().split()) # N: 동전의 종류 개수, K: 만들어야 할 금액
coin_info = set()  # 중복 제거를 위해 집합 사용
for _ in range(N):
    coin_info.add(int(input().rstrip()))

bfs(0)

