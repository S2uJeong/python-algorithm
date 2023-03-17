# 책 모범 답안
 # 이차원배열 위에서 움직이는 문제에서 step 표현법 익힐 것
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1 # 주어진 문제의 체스판이 1~8 기준이라서 1을 더해줌. ord 활용법 참고 (문자 -> 정수)

steps = [(1,-2),(-1,-2),(1,2),(-1,2),(2,-1),(2,1),(-2,-1),(-2,1)] #[]는 리스트, ()는 튜플

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >=1 and next_row <= 8 and next_col >=1 and next_col <= 8 :
        result += 1

print(result)

# ===== 내가 푼 문제 (비효율,,) ======
input = input()

col = input[0]
row = int(input[1])

# 알파벳으로 입력되는 열의 정수화
if col == 'a':
    col = int(1)
elif col == 'b':
    col = int(2)
elif col == 'c':
    col = int(3)
elif col == 'd':
    col = int(4)
elif col == 'e':
    col = int(5)
elif col == 'f':
    col = int(6)
elif col == 'g':
    col = int(7)
else : col = int(8)

count = 0

if (row + 1 <= 0 or row + 1 >= 8) or (col-2 <= 0 or col-2 >= 8): pass
else : count += 1

if (row-1 <= 0 or row-1 >= 8) or (col-2 <= 0 or col-2 >= 8): pass
else : count += 1

if (row+1 <= 0 or row+1 >= 8) or (col+2 <= 0 or col+2 >= 8): pass
else : count += 1

if (row-1 <= 0 or row-1 >= 8) or (col+2 <= 0 or col+2 >= 8): pass
else : count += 1

if (row + 2 <= 0 or row + 2 >= 8) or (col-1 <= 0 or col-1 >= 8): pass
else : count += 1

if (row + 2 <= 0 or row + 2 >= 8) or (col+1 <= 0 or col+1 >= 8): pass
else : count += 1

if (row - 2 <= 0 or row - 2 >= 8) or (col-1 <= 0 or col-1 >= 8): pass
else : count += 1

if (row - 2 <= 0 or row - 2 >= 8) or (col+1 <= 0 or col+1 >= 8): pass
else : count += 1

print(count)