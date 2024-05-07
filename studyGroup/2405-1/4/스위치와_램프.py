"""
1. 스위치 순서 대로 해당 스위치가 켤 수 있는 램프를 집합 자료구조에 넣는다.
2. N-1번째 턴까지 집합 자료구조의 길이가 램프의 길이와 같아지면 램프를 모두 켤 수 있다
스위치를 차례로 할 수 있는 이유 : 스위치 순서 상관 없이 다 켜져야 하기 때문
오답 : 어떤 스위치를 어떤 순서로 누를 지 모른다
===============================
1. 콤비네이션을 통해 스위치 N-1개를 뽑는 경우를 다 뽑는다.
2. 해당 스위치를 눌렀을때 램프가 다 켜지는지 확인
3. set 자료구조 사용
4. 성능개선 : 다 보기 전에 이미 set의 길이가 M이 됐을 떄 .
오답 : 왜 오답이지? 문제를 잘못 이해했나.
===============================
"""

import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
lamps = [list(map(int,input().split())) for _ in range(N)]
switch_combis = list(combinations(range(N),N-1))
lights = set()
isPossible = True

for switch in switch_combis: #  switch = (1,2,3,5) 와 같이 스위치 숫자가 담김
    isPossible = True   
    lights.clear()
    for s in switch:
        for j in range(1,len(lamps[s-1])):
           lights.add(lamps[s-1][j])
           if len(lights) == M:
               break
    if len(lights) < M:
        isPossible = False

if isPossible :
    print(1)
else :
    print(0)
