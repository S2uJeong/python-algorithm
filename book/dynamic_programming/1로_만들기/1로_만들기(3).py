N = int(input())

d = [0] * 30001
for i in range(2,N+1):
    # 1 더했을 때
    d[i] = d[i-1] + 1
    # 분기 시작 (나누어 떨어지는 수에 따라)
    if i % 2 == 0 :
        if d[i] < d[i//2] +1:
            print(i)
        d[i] = min(d[i], d[i//2] +1)
    elif i % 3 == 0 :
        if d[i] < d[i//3] +1:
            print(i)
        d[i] = min(d[i], d[i//3] +1)
    elif i % 5 == 0 :
        if d[i] < d[i//5] +1:
            print(i)
        d[i] = min(d[i], d[i//5] +1)

print(d[N])
