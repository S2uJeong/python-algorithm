# 정사각형 회전
def rotate_a_matrix_by_90_degree(matrix) :
    n = len(matrix) # 행 길이
    m = len(matrix[0]) # 열 길이
    result = [[0] * n for _ in range(m)] # 결과 리스트 (기존과 행,열이 바뀌어 있음)
    for i in range(n) :
        for j in range(n):
            result[j][n-i-1] = matrix[i][j]
    return result

matrix = [[0,0,1,0], [0,1,0,1], [0,1,0,0], [1,1,1,0]]
print(rotate_a_matrix_by_90_degree(matrix))

