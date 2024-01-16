N, T = map(int,input().split())
songs = list(map(int,input().split()))

def sum_list(lt,rt,p_list):
    res = 0
    for i in range(lt,rt+1):
        res += p_list[i]
    return res

# lt,rt의 기준이 될 노래의 총 길이를 변수에 대입한다. (최소화하는 대상은 최소용량이므로)
total = sum(songs)
res = 1e12
lt, rt = 1, total  # 노래 길이는 1분 부터 시작
while lt <= rt :
    cnt = 0
    sum = 0
    mid = (lt + rt) // 2
    print(f'mid : {mid}')
    for idx,lang in enumerate(songs) :
        if lang <= mid : # 이거 안 넣어서 버그 났었음
            if sum + lang > mid:
                cnt += 1
                sum = 0
            sum += lang
            if idx == len(songs)-1 and sum != 0:
                 cnt += 1
            print(f'{idx}번째 노래 진행중 lang : {lang} , sum:{sum} , cnt : {cnt}')
        else :
            break
    print(f'mid : {mid}, cnt = {cnt}')
    if mid >= max(songs) and cnt <= T :
        rt = mid - 1
        if res > mid:
            res = mid
    else :
        lt = mid + 1
    print(f'lt = {lt}, rt ={rt}')

print(res)
