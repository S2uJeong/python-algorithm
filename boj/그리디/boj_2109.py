"""
우선순위큐 사용해서,
더 쏀 PAY가 들어오는데 LENGTH가 해당 날짜보다 크면 제일 작은 걸 뺴고, 해당 pay를 넣는다.
만약 length가 넘지 않으면 그냥 넣는다.
이는 빠듯한 날짜의 강연일수록, pay가 작을수록 정렬된 list를 순회하며 answer에 넣으므로 정당하다.

우선순위 큐는 정답을 모아놓는 자료구조에 적용하며, 최소힙으로 만들어야 한다.
"""
import sys
import heapq
input = sys.stdin.readline
N = int(input().rstrip())
pays = [list(map(int,input().split())) for _ in range(N)]
pays.sort(key = lambda x : (x[1],x[0]) ) # 제한 날짜가 빠를 수록 -> pay가 작을 수록

answer_list = []

for pay, day in pays:
    if day <= len(answer_list):
        heapq.heappop(answer_list)
        heapq.heappush(answer_list, pay)
    else :
        heapq.heappush(answer_list, pay)

print(sum(answer_list))




















