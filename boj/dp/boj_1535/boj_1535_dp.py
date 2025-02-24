"""
배낭 문제 변형

"""

N = int(input())
lst = list(zip(map(int, input().split()), map(int,input().split())))
lst.sort(reverse=True) # value 기준 내림차순

dp = {0:0} # key = 기쁨(value), value = key를 만들기 위한 체력(weight)

# (w,v) 조합을 탐색하며 dp 업데이트하며 dp는 현재 가치 합 -> 최소무게를 저장
for weight, value in lst:
    data = {}
    for v,w in dp.items():
        v += value
        w += weight

        if dp.get(v, 100) > w: # 같은 value를 가지는데 지금 weight가 기존 dp것보다 작으면 update한다.
            data[v] = w
    dp.update(data)

print(max(dp.keys()))