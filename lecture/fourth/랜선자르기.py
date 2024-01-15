have, need = map(int,input().split())

lines = [ int(input()) for _ in range(have)]
max_lang = max(lines)
lt,rt = 1, max_lang
res = 0
while lt <= rt :
    mid = (rt + lt) // 2
    cnt = 0
    for line in lines:
        if line // mid > 0 :
            cnt +=  line // mid
    if cnt < need:
        rt = mid - 1
    else :
        if mid > res :
            res = mid
        lt = mid + 1

print(res)


