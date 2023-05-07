import sys
input = sys.stdin.readline

list = [0] * 10001

# 들어오는 수를 계수 리스트에 담는다.
for i in range(int(input())):
    x = int(input().strip())
    list[x] += 1

# 차례대로 출력한다.
for i in range(1,10001):
    while list[i] != 0 :
       # print(i)
        sys.stdout.write(str(i) + '\n')
        list[i] -= 1

# print(*list, sep='\n')
