"""
우승 조건 : 필요한 승수, 경기 진행 순서는 정해져있음.
1. 같은 손동작이면 진행 순서상 뒤인 사람이 이긴다. => 지우, 경희 민호 : 지우는 비기면 무조건 진다.
2. 토너먼트 방식

인싸 가위바위보의 상성표와 손동작의 순서가 주어졌을 때 지우가 모든 손동작을 다르게 내어 우승할 수 있는지 판단하는 프로그램

방법
1. 지우의 손 족보를 permu로 구한다.
2. permu 마다 승 승부 결과를 구현해 지우가 우승할 수 있는지 본다.
"""
import sys
input = sys.stdin.readline
from itertools import permutations
# 입력
N, K = map(int,input().split()) # 손 동작 수, 우승을 위해 필요한 승수
datas = [list(map(int, input().split())) for _ in range(N)] # 계보 : i기준, j를 이긴다 2 비긴다 1 진다 0
k_list = list(map(int,input().split())) # 경희
m_list = list(map(int,input().split())) # 민호
j_list = [i+1 for i in range(N)] # 지우

# 문제 풀이
def dfs(py1, py2, index, win, whole_hands) :
    global result
    # 지우가 이김
    if win[0] == K :
        result =1
        return
    if win[1] == K or win[2] == K :
        return
    if index[0] == N : # 앞으로 낼 새로운 손모양이 없음
        return

    py3 = 3 - (py1 + py2) # 다음 출전자
    hand1 = whole_hands[py1][index[py1]] - 1 # user1이 낼 손모양
    hand2 = whole_hands[py2][index[py2]] - 1
    index[py1] += 1
    index[py2] += 1
    if datas[hand1][hand2] == 2 or (datas[hand1][hand2] == 1 and py1 > py2): # user1이 이긴다.
        win[py1] += 1
        dfs(py1, py3, index, win, whole_hands)
    elif datas[hand2][hand1] == 2 or (datas[hand2][hand1] == 1 and py2 > py1): # user2이 이긴다.
        win[py2] += 1
        dfs(py2, py3, index, win, whole_hands)

for permu in permutations(j_list, N):
    whole_hands = [permu, k_list, m_list] # (이중 리스트) 지우, 경희, 민호 순 (경기진행 순서)
    index = [0,0,0] # 어떤 손모양을 낼지 (손 순서 차례대로 +1 cnt하는 용도 )
    win = [0,0,0]
    result = 0
    dfs(0,1,index, win, whole_hands)
    if result == 1 :
        print(1)
        break
else :
    print(0)





