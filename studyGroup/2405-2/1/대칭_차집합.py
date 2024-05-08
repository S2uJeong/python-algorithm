"""
해쉬 이용
key : 원소의 값, value: A,B에 해당 원소의 갯수 합 (1,2)
hash 길이(합집합) - hash에서 value가 2이상인 것의 길이(교집합)
"""
A, B = map(int,input().split())
A_arr = list(map(int,input().split()))
B_arr = list(map(int,input().split()))

d = dict()

for a in A_arr:
    d[a] = 1

for b in B_arr:
    if b in d.keys():
        d[b] += 1
    else :    # else 빠뜨렸다가, 파이썬 딕셔너리는 값이 덮어진다는 것 때문에 버그남
        d[b] = 1
M = 0  # 교집합 개수
for i in d.values():
    if i >= 2:
        M += 1

print(len(d)-M)





"""
대칭 차집합은 두 집합의 합집합에 교집합을 뺸것과 같다
==> 시간 초과 
"""
def fail() :
    A, B = map(int,input().split())
    A_arr = list(map(int,input().split()))
    B_arr = list(map(int,input().split()))

    # 합집합
    set_arr = set()
    set_arr.update(A_arr)
    set_arr.update(B_arr)

    # 교집합
    cross_arr = []
    for i in A_arr:
        if i in B_arr:
            cross_arr.append(i)

    print(len(set_arr) - len(cross_arr))