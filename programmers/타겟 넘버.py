res = 0
def solution(numbers, target):
    global res
    total = sum(numbers)
    n = len(numbers)
    DFS(0,0,0, target, numbers, total, n)
    return res

# 수학 방법 : 모든 경우의 수를 뽑아서 더해보고, 타겟과 맞으면 전역변수 cnt 값을 올려준다.
# 가지 치기 : 남은 숫자를 다 안 썼다고 했을 때에도, 총 더한 값이 target 이상이면 더 탐색하지 않는다.
def DFS(L, sum, tsum, target, numbers, total, n):
    global res
    if sum + (total - tsum) < target:
        return
    if L == n :
        if sum == target:
            res += 1
        return
    else :
        # 다음 노드의 수를 +로 더한다.
        DFS(L+1, sum + numbers[L], tsum + numbers[L], target, numbers, total, n )
        # 다음 노드의 수를 -로 더한다.
        DFS(L + 1, sum + (-1*numbers[L]), tsum + numbers[L], target, numbers, total, n)


#print(solution([1, 1, 1, 1, 1], 3))
#print(solution([4,1,2,1], 4))