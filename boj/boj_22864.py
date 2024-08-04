"""
피로도
1시간 마다의 상태치를 주며, maximum이 되기 전에 피로를 풀어주어야 한다.
하루에 최대 할 수 있는 일의 양을 반환해야 하며 하루는 24시간이다.
"""
plus, value, minus, maximum = map(int,input().split())

crt_hp = 0
result = 0
crt_time = 0

while True:
    if crt_time >= 24:
        break

    if crt_hp + plus > maximum:
        crt_hp = max(0, crt_hp - minus)
    else:
        crt_hp += plus
        result += value

    crt_time += 1

print(result)