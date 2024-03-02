import sys
sys.setrecursionlimit(100000)

def f(n):
    if n <= 2 :
        return 1
    else :
        return f(n-2) + f(n-1)

# print(f(int(input())))

memo = {}
def use_memo(num):
    if num in memo:
        return memo[num]

    if num == 0:
        memo[0] = 0
        return memo[0]
    elif num == 1 :
        memo[1] = 1
        return memo[1]
    else :
        memo[num] = use_memo(num-1) + use_memo(num-2)
        return memo[num]

print(use_memo(int(input())))

