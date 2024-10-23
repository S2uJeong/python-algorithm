def dfs(idx, permu):
    if len(permu) >= M :
        print(*permu)
        return
    if idx >= N:
        return
    permu.append(nums[idx])
    dfs(idx+1, permu)  # 해당 수를 포함 하여 전개

    permu.pop()
    dfs(idx+1, permu)  # 해당 수를 포함 하지 않고 전개

N, M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
dfs(0, [])
