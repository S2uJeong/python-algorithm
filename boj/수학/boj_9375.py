"""
들어오는 input 값을 해시 자료구조에 넣고 그 값에 따라 조합 계산을 통해 반환한다.

N이 0일 때 print(0)으로 예외처리 해주니까 틀린 것으로 나와서 꽤 많이 틀림..
"""
T = int(input())
for _ in range(T):
    N = int(input())
    items = {}
    for _ in range(N):
        i, kind = input().split()
        if kind in items.keys():
            items[kind] += 1
        else :
            items[kind] = 1

    # 경우의 수 계산
    result = 1
    for val in items.values():
        result *= (val+1) # 1은 해당 종류의 의상을 안 입었을 때를 고려

    print(result-1) # 알몸상태 제외