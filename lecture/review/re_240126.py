# 10진수 -> n진수 변환 함수
def DFS(num, base):
    if num == 0 :
        return
    else :
        DFS(num//base,base)
        print(num%base, end='')

print('[10진수 -> n진수] 10진수 수와 n을 공백을 기준으로 한 줄에 입력해주세요.')
num,base = map(int,input().split())
print(f'{num}을 {base}진수로 바꾼 값은?')
DFS(num,base)

print('1부터 n까지의 부분집합을 구하는 함수입니다. n을 입력하여 주세요.')
n = int(input())
def subset(v):
    status = [0] * (n+1)
    if v > n :
        for idx,val in enumerate(status):
            if val == 1 :
                print(idx,end=' ')
        print()
    else :
        status[v] = 1
        subset(v+1)
        status[v] = 0
        subset(v+1)



subset(1)
