'''
N자리 숫자가 주어졌을 때, 숫자 K개를 지워서 얻을 수 있는 가장 큰 수 구하는 프로그램 작성

- deque 활용 (왼쪽부터 채운다)
- deque에 주어진 숫자의 맨 왼쪽수를 하나 넣어 둔다.
- 주어진 숫자를 두번째 칸부터 왼쪽에서 오른쪽으로 탐색하며, deque[-1]보다 현재 수가 클 때까지 deque.pop()을 한 뒤 현재 수를 넣는다.
'''
from collections import deque

def solution():
    result = deque([ num_string[0] ])
    cur = 1
    remove_count = K  # 남은 제거 횟수

    while cur < N:
        while remove_count and result and int(result[-1]) < int(num_string[cur]) :
            result.pop()
            remove_count -= 1

        result.append(num_string[cur])
        cur += 1

    while len(result) > N-K :
        result.pop()

    return result


N, K = map(int,input().split())
num_string = input()
result = solution()

for char in result:
    print(char, end='')