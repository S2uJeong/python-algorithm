s, e = map(int,input().split())

permus = []
tmp = 1
cnt = 1

while True :
    if len(permus) == e :
        break
    permus.append(tmp)
    cnt -= 1
    if cnt == 0:
        tmp += 1
        cnt = tmp

print(sum(permus[s-1:e]))

