# fourth > [이분검색] 뮤직비디오.py

song_N, cd_N = map(int, input().split())
songs = list(map(int, input().split()))

lt, rt = max(songs), sum(songs)
res = 0
while lt <= rt:
    print(f'lt = {lt}, rt = {rt}')
    mid = (lt + rt) // 2
    sum = 0
    cd_cnt = 1
    for song in songs:
        if song > mid:
            cd_cnt = 0
            print(f'하나의 노래가 용량보다 커요! --- cd_cnt = {cd_cnt}')
            break
        else:
            if sum + song > mid:
                cd_cnt += 1
                sum = song
            else :
                sum += song
            print(f'song - {song}, sum = {sum}, cd_cnt = {cd_cnt}')

    if cd_cnt > cd_N:
        lt = mid + 1
    else:
        res = mid
        rt = mid - 1

print(res)


# fourth > [그리디] 증가수열 만들기.py
def make_increase_nums():
    print('입력될 숫자들의 갯수를 적어주세요 : ', end ='')
    N = int(input())
    print('숫자를 공백을 기준으로 한줄로 아래에 적어주세요')
    nums = list(map(int,input().split()))

    lt,rt = 0, N-1;
    res = ""
    max = -1 # 증가하는 수열의 가장 오른쪽 수가 저장 될 변수

    while lt <= rt :
        tmp = []
        if nums[lt] > max :
            tmp.append((nums[lt],'L'))
        if nums[rt] > max :
            tmp.append((nums[rt],'R'))
        tmp.sort()
        if len(tmp) == 0:
            break
        else :
            # 0 : sort를 했으므로 리스트에서 제일 작은 숫자가 위치한 곳이다
            max = tmp[0][0]
            res += tmp[0][1]
            if tmp[0][1] == 'L':
                lt += 1
            else :
                rt -= 1
    print(f'증가수열의 길이는 {len(res)}입니다.')
    print(f'증가수열이 만들어진 방향은 {res} 입니다')


# ======= 함수 실행 =========
# make_increase_nums();
