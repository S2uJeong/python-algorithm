"""
출력 : 이름은 사전순, 비율은 소수점 4까지 반올림
dictionary 사용 해서 갯수 하나씩 세는 것으로.

🔴딕셔너리 정렬은 sort로 안되고 sorted로만 됨
🔴반올림에서 고민 많이 했었는데,, 그냥 서식 문자열 사용하면 간단함. round말고 이거 쓰기
"""
import math
import sys
input = sys.stdin.readline

trees = dict()
total_cnt = 0
while True:
    tree = input().rstrip()
    if tree == '':
        break
    total_cnt += 1
    if tree in trees.keys():
        trees[tree] += 1
    else :
        trees[tree] = 1

result = sorted(trees.items())

for tree,cnt in result:
    val = (cnt/total_cnt) * 100
    print("%s %.4f" %(tree, val))
