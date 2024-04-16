"""
- 열림 조건 : 자물쇠를 뜻하는 테이블의 값이 다 1이여야 한다.
- 방법 :
1. key 테이블을 오른쪽 방향으로 4번 돌리면서
    1-1. key테이블이 위,왼쪽에서 시작하여 key가 자물쇠 위에 한칸이라도 겹치면 값을 더해 자물쇠 테이블의 val이 다 1인지 확인한다.
- 아이디어 :
    자물쇠, 열쇠의 자료 크기를 3배로 만들고, 원래 값은 중앙에 옮긴다.
    이 방법을 이용하면, 한칸이라도 겹칠시 탐색하는 것을 쉽게 할 수 있다.
"""
'''
check(metrix) : 이차원 배열의 값이 다 1인지 확인한다.  
return BOOL
'''
def check(metrix):
    locK_length = len(metrix) // 3
    for i in range(locK_length, locK_length * 2):
        for j in range(locK_length, locK_length * 2):
            if metrix[i][j] != 1 :
                return False
    return True
'''
rotate(matrix) : 열쇠를 90도 회전한다.
return matrix
'''
def rotate(matrix):
    n = len(matrix) # 행의 길이
    m = len(matrix[0]) # 열의 길이
    new_matrix = [[0] * n for _ in range(m)] # 회전된 테이블
    for i in range(n):
        for j in range(m):
            new_matrix[j][n-i-1] = matrix[i][j]
    return new_matrix

def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 확장한 자물쇠 구현
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]
    # 시작
    for _ in range(4):  # 90 회전 횟수를 의미 90 * 4 = 360도 이므로 4번
        key = rotate(key) # key를 돌린다.
        # 아래 이중 for문은 확장된 자물쇠와 key 간의 인덱스를 비교시 맞춰주기 위해 존재
        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 열쇠를 다시 뺀다.
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False