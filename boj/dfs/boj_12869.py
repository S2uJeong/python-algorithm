"""
dfs 이용 해서 모든 경우의 수를 고려
N * N * N ... 이고, 체력은 늘 60보다 작거나 같으므로 60 * 20 * 7 보단 경우의 수가 작다.

오답노트
1. count 값을 이용한 메모제이션 => 시간초과
2. count, 현재 army 체력 상태 두 조건을 이용한 메모제이션 => 통과
3. 문제 자체가 count가 제일 적은 최단 경로를 추출하라는 문제여서 bfs가 시간 성능적으로 더 괜찮은 선택이었다.

"""
from itertools import permutations
import sys
input = sys.stdin.readline

def fight(cur_army, selected_pattern):
    updated_army = []
    for i in range(len(cur_army)):
        updated_army.append(cur_army[i] - selected_pattern[i])
    return updated_army

def is_annihilation(cur_army):
    return all(army <= 0 for army in cur_army)
def dfs(count, cur_army):
    # 현재 상태를 튜플로 변환하여 메모이제이션 키로 사용
    army_tuple = tuple(cur_army)
    # 이미 방문한 상태인지 확인 (메모제이션 확인)
    if army_tuple in memo and memo[army_tuple] <= count:
        return
    memo[army_tuple] = count

    if is_annihilation(cur_army):
        global answer
        answer = min(count, answer)
        return

    for pa in patterns:
        next_army = fight(cur_army, pa)
        dfs(count+1, next_army)

def make_patterns(selected_damages, N):
    return list(permutations(selected_damages, N))

damages = [9,3,1]
N = int(input().rstrip())
army = list(map(int,input().split()))
patterns = make_patterns(damages[:N], N) # 데미지가 내림차순으로 정렬되어 있기 때문에, 크게 때릴수 있는거 우선으로 한다. 한 캐릭터당 한 턴만 때릴 수 있기 때문에 조건 추ㅊ

answer = float('inf')
memo = {} # 현재 군대의 잔여 체력량을 key로 count를 value로 가진 memo 딕셔너리
dfs(0, army)

print(answer)