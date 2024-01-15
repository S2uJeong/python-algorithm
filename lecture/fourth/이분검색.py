N, target = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()
lt, rt = 0, N-1
while lt <= rt:
    if nums[rt//2 +1] > target:
        lt = rt//2 +1
    elif nums[rt//2 +1] < target:
        rt = rwt//2 -1
    else :
        rt//2

print(lt+1)
