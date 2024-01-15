N, target = map(int,input().split())
nums = list(map(int,input().split()))

nums.sort()
lt, rt = 0, N-1
i = 0
while lt <= rt:
    i += 1
    mid_idx = (rt+lt)//2
    print(f'{i}번째 rt = {rt}, lt = {lt}, mid_idx = {mid_idx}')
    if nums[mid_idx] > target:
        rt = mid_idx - 1
    elif nums[mid_idx] < target:
        lt = mid_idx + 1
    else :
        break
print(mid_idx+1)

