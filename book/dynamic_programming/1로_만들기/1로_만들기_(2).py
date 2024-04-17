# 복습
import sys
input = sys.stdin.readline

target = int(input())

d = [0] * 30001 # 입력되는 target은 1~30,000의 값을 가진다.

for i in range(2,target+1):
    d[i] = d[i-1] + 1  # 1로 빼는 것에 대한 횟수 1 더하기, 무조건 들림

    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[target])

# if 문에 2->3->5 순으로 쓰여진 이유를 잘 생각해보면 좋음