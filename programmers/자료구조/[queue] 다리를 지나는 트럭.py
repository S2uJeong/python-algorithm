# 다리의 길이 1당 1초가 걸린다.
# 트럭이 절반 걸쳐 있을 땐 고려하지 않는다.
# 다리를 건너는 트럭 최대 차량 댓수 : 도로 길이, 도로 최대 무게 고려
from collections import deque


def solution(bridge_length, weight, truck_weights):
    sc = 0  # 걸린 시간 ( 도로 1칸 = 1초 )
    bl = deque([0] * bridge_length)  # 다리 위를 표현할 큐
    truck_weights = deque(truck_weights)

    tmp_w = 0
    while len(truck_weights) != 0 :

        sc += 1
        tmp_w -= bl.popleft() # point! 차가 도로 길이에 다다르지 않아도, 0으로 도로 큐를 채워놨어서
        # 계속 제일 왼쪽에 있는 것을 빼서 현재 도로 무게에 더해도 의미가 없어서 복잡한 수식이 필요없어진다.

        if tmp_w + truck_weights[0] <= weight:
            tmp_w += truck_weights[0]
            bl.append(truck_weights.popleft())
        else :
            bl.append(0)
    sc += bridge_length # 마지막에 도로에 들어온 차량이 끝까지 가는 시간을 더해준다.

    return sc

print(solution(2,10,[7,4,5,6]))