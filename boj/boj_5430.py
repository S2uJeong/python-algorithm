"""
AC는 정수 배열에 연산을 하기 위해 만든 언어
이 언어에는 두 가지 함수 R(뒤집기), D(첫번째 수 버리기)가 있음
    - 배열이 비었는데 버리면 에러 발생

뒤집는 동작을 idx 1, -1로 구분하여 표시 (1: 정방향, -1: 뒤집은 방향)
idx 위치에 따라 뒤에서 값을 뺄지, 앞에서 뺼지 선택 후
명령이 끝나면 idx 위치에 따라 출력
"""
from collections import deque
import sys

input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    command = input().rstrip()
    # 배열 입력
    arr_length = int(input().rstrip())
    nums = input().rstrip()[1:-1] # 대괄호 제거
    if len(nums) < 1:
        print("error")
        break
    else:
        nums = deque(nums.split(","))

    # command 실행
    direction_flag = 1 # 처음엔 정방향
    for c in command:
        if c == 'R':
            direction_flag *= -1
        if c == 'D':
            if len(nums) < 1 :
                break
            if direction_flag == 1: # 정방향이면
                nums.popleft()
            else : # 역방향이면
                nums.pop()

    # 출력
    if len(nums) < 1:
        print("error")
    else:
        if direction_flag == 1: # 정방향이면
            print(f'[{",".join(nums)}]')
        else:
            nums.reverse()
            print(f'[{",".join(nums)}]')