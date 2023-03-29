def solution(n): # n : 떨어져 있는 거리
    battery = 1 # 거리 이동하는데 사용한 배터리 양
    # 처음엔 무조건 한 칸 이동해야만 순간이동이 가능하기 때문에 점프를 한번 했다고 가정하고 시작.
    while n > 1:
        if (n%2 == 0) :
            n /= 2
        else:
            battery += 1
            n -= 1

    return battery

print(solution(5000))
