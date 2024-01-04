T = int(input())

for _ in range(T):
    N,s,e,k = map(int,input().split())
    nums = list(map(int,input().split()))

    sorted_nums = nums[s-1:e]
    sorted_nums.sort()
    print(sorted_nums[k-1])
