"""
https://codeup.kr/problem.php?id=1901
"""
K = int(input())

def dfs(n) :

    print(n)

    if n == K :
        return

    dfs(n+1)
    """
    흥미로운 점 발견!!! dfs 함수 이후의 문장은 또 반대로 실행 됨. 데칼코마니의 형태
    그리고 종료 조건문에 맞는 순간의 n값은 dfs 이후 코드에 반영되지 못함을 발견.
    예를 들어 n = 3 이면, 밑의 print 문은 2, 1 순으로 찍는다. 
    """
    print(">?>>> 여기는 언제나와?" + str(n))
dfs(1)