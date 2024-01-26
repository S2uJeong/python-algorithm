import sys
# 아이디어1 : 하나의 부분집합만 만들고, 그 부분집합에 들어가 있지 않은 수는 다른 부분집합에 들어가 있다고 가정함
n = int(input())
nums = list(map(int,input().split()))

# 아이디어2 : 누적 수를 파라미터로 받는다.
#       3 : sum으로만 부분집합 포함 여부를 표현한다.
#       4 : list total - sum = sum 이면 True다.
total = sum(nums)
def DFS(L,sum):
    if sum > total // 2 :
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0) # --> 함수가 아닌 프로그램 자체를 죽인다.
    else:
        DFS(L+1,sum+nums[L]) # 해당 값을 이용한다.
        DFS(L+1,sum) # 해당 값을 이용 안한다.

DFS(0,0)
print("NO")



