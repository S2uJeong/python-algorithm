"""
체력이 0이하가 되지 않게 얻을 수 있는 기쁨의 max 수치
체력의 기본값은 100이다.
1 <= N <= 20

dfs
- 매 순간마다 인사 하느냐 안 하느냐로 판단하여 최종적으로 더 높은 것으로 select
- 전개 중에 체력이 100이상 필요하면 return 한다.
- O(2**N), N이 20이하이므로 최악의 경우 1_048_576

dp로 개선할 수 있을것 같은데 떠오르지 않음.
"""
N = int(input()) # 사람의 수
strength = list(map(int,input().split())) # 잃는 체력
happiness = list(map(int,input().split())) # 얻는 기쁨

result = 0 # 인사 못하면 기쁨은 0으로 반환된다.
def dfs(cur_strength, cur_happiness, idx):
    global result
    if cur_strength >= 100:
        return
    if idx >= N:
        result = max(result, cur_happiness)
        return
    dfs(cur_strength + strength[idx], cur_happiness + happiness[idx], idx+1) # 현재 idx의 사람에게 인사한다.
    dfs(cur_strength, cur_happiness, idx+1) # 인사 안 한다.


dfs(0,0,0)
print(result)