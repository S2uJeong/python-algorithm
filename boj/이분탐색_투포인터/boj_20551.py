"""
원소의 크기도 크고, 질문도 여러번 한다. => O(N)으로 문제를 풀어야 한다.
"""
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A_arr = [int(input()) for _ in range(N)]
A_arr.sort() # O(NlogN)
"""
이진탐색
"""
for _ in range(M):
    # 매 테스트케이스마다 초기화
    target = int(input())
    s = 0
    e = N - 1  # (N:원소의 개수)
    result = -1
    # 이진탐색 시작
    while s <= e :
        mid = (s+e) // 2
        if A_arr[mid] == target:
            result = mid
            e = mid # - 1 # 더 먼저 나온 같은 숫자가 있을 수 있으므로 : 처음에 -1 붙여서 틀림,,
        elif A_arr[mid] > target:
            e = mid - 1
        else :
            s = mid + 1
    print(result)

"""
딕셔너리 이용 
"""
def use_dictionary() :
    # 딕셔너리 key값을 문자로하고, value를 처음 나온 index로 넣는다.
      # key에 이미 있는 값이면 continue
    dicts = dict()
    for i in range(len(A_arr)) :
        if A_arr[i] not in dicts.keys():
            dicts[A_arr[i]] = i

    # 질문 받으면서 바로 index or -1 출력
    for _ in range(M):
        quest = int(input())
        if quest not in dicts.keys():
            print(-1)
        else :
            print(dicts[quest])
