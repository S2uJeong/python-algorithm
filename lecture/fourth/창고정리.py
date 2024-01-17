N = int(input()) # 바닥 가로 길이
arr = list(map(int,input().split())) # 상자 높이
M = int(input()) # 박스 이동 횟수
cnt = 0
while cnt < M:
    arr.sort() # arr[0] : 제일 박스가 적은곳
    arr[0] += 1
    arr[-1] -=1
    cnt += 1

print(max(arr) - min(arr))

