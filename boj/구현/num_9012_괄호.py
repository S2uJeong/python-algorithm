# 괄호의 여닫이가 있어야 Yes, 아니면 No
# 열었다 -> count +1 닫았다 -> -1 마지막에 0이 되면 YES 아니면 NO
# 순서는 어떻게 보장하지? )()(  이것도 count는 0인데
# count가 -1로 떨어지면 아웃? g

import sys
input = sys.stdin.readline
print = sys.stdout.write

for _ in range(int(input())):
    count = 0  # 🔴count 초기화 시점 주의
    result = ''
    str_list = list(input().split())

    for i in str_list[0] : # 🔴 list를 쓸 때에는 range 안써도 됨 + [0] 있고 없고의 차이 유의

        if count == -1:
            break
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1

    if count == 0 :
        result = 'YES'
    else :
        result = 'NO'

    print(result + '\n')




