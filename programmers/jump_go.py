n = int(input())
ans = 0
battery = 0

while True:
    # 종료 조건
    if n - ans == 0:
        break

    ans += 1  # jump
    battery += 1

    if (n - ans * 2) >= 0:
        ans = ans * 2  # go , 현재 좌표


print(battery)

# https://school.programmers.co.kr/learn/courses/30/lessons/12980
# ====== 아이디어 =======
# 1. 반대로 간다.
#