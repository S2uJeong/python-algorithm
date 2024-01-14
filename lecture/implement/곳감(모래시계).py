import time

T = int(input())
in_list = [list(map(int,input().split())) for _ in range(T)]
N = int(input())

start_time = time.time()

for i in range(N):
    row, way, amt = map(int,input().split())

    if way == 0: # 왼쪽으로
        for j in range(amt):
            in_list[row-1].append(in_list[row-1].pop(0))
    else:
        for j in range(amt):
            in_list[row-1].insert(0,in_list[row-1].pop())

end_time = time.time()
print(f'{T*T}개 자료,{N}개의 명령에서 걸린시간 :{end_time - start_time:.5f} sec')

# 모래시계 모양으로 합한 수 구하기

s, e = 0, T
res = 0
for i in range(T):
    if i < T//2 :
        for j in range(s,e):
            res += in_list[i][j]
            s += 1
            e -= 1
    else :
        for j in range(s,e):
            res += in_list[i][j]
            s -= 1
            e += 1

print(res)