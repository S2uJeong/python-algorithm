'''
stack을 활용하면 더 쉽게 할 수 있다.
'''

def solution():
    remove_cnt = K
    stack = [nums[0]]

    cur = 1
    while cur < N:
        while remove_cnt > 0 and stack and stack[-1] < nums[cur] :
            stack.pop()
            remove_cnt -= 1
        stack.append(nums[cur])
        cur += 1

    return stack[:N-K]


N, K = map(int,input().split())
nums = list(map(int,input()))
result = solution()
for num in result:
    print(num, end ='')



