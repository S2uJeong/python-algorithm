# https://www.acmicpc.net/problem/18406
# String으로 받는 방법
def stringMethod() :
    N = input()

    left_str = N[0:(len(N)//2)]
    right_str = N[len(N)//2 : len(N)]

    sum_l, sum_r = 0,0
    for i in range(len(left_str)):
        sum_l += int(left_str[i])
        sum_r += int(right_str[i])

    if sum_r == sum_l:
        print("LUCKY")
    else :
        print("READY")

# 입력받을 떄 아예 list로 받는 방법
def listMethod() :
    nums = list(map(int,input()))
    print(nums)
    sum_l, sum_r = 0,0
    for i in range(len(nums)//2):
        sum_l += nums[i]
        sum_r += nums[-i-1]
    if sum_l == sum_r :
        print("LUCKY")
    else :
        print("READY")

listMethod()