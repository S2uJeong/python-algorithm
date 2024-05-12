"""
백트래킹 + 완전 탐색
- 주어진 책을 고르냐, 안 고르냐 선택하여 dfs()진행
  - 현재 책을 선택하면, 주어진 T에서 해당하는 알파벳을 뺴주고, 금액을 증가시켜 재귀
  - 선택하지 않으면, 깊이만 1 증가하고 재귀호출
- if n개의 책을 모두 탐색했다면, return
    - 만들고자 한 단어 알파벳이 다 나왔으면 갱신

- dict 만들어서 있는지 없는지 확인하고 +1 하기 힘들어서 알파벳 리스트를 만듬
    - idx : C - 'A' / ex) A면 인덱스0, B면 인덱스 1
    - val : 알파벳 출현 횟수

- 재귀 만드는 법 :
   - 해당 책을 선택 하고 안 하고를 주어진 list의 index 흐름에 따라 level로 표현한 것
"""
# 입력
T = input()
N = int(input())
books = []
for _ in range(N):
    price, name = input().split()
    books.append([int(price), name])
# 문제를 위한 자료구조
select_alpa = [0] * 26 # 알파벳은 26개, 선택된 책이 지닌 알파벳 갯수를 나타냄
T_alps = [0] * 26 # 만들어야 하는 값의 알파벳 개수

for c in T:
    tmp = ord(c) - ord('A')
    T_alps[tmp] += 1

result = INF = 1e9
def dfs(n, price):  # n번째 책 (단계) , 가격
    global result
    if n == N : # 책 마지막까지 탐색 완료
        if (is_include_all()):
            result = min(result, price)
        return
    # n번째 책을 선택했다.
        # 선택한 알파벳 수 늘려주기
    for c in books[n][1]:
        tmp = ord(c) - ord('A')
        select_alpa[tmp] += 1
        # dfs 호출
    dfs(n+1, price+books[n][0])
        # 호출 후 선택 알파벳 수 초기화
    for c in books[n][1]:
        tmp =ord(c) - ord('A')
        select_alpa[tmp] -= 1

    # n번째 책을 선택하지 않는다.
    dfs(n+1, price)
def is_include_all():
    for i in range(26):
        if T_alps[i] > select_alpa[i]:
            return False
    return True


dfs(0,0)
if result == INF:
    print(-1)
else :
    print(result)