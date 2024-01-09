def get_divisor_cnt(p_num):
    cnt = 0
    for i in range(1,p_num+1):
        if p_num % i == 0:
            cnt += 1
    return cnt

def get_int_to_str(p_str):
    result_list = []
    for c in p_str:
        if c in ['1','2','3','4','5','6','7','8','9','0'] :
            result_list.append(c)
    return result_list
def first_try():
    input_str = input()
    nums = get_int_to_str(input_str)
    num = int(''.join(nums))
    return num, get_divisor_cnt(num)

print(first_try())

def eaxmple():
    s = input()
    res = 0
    for x in s :
        if x.isdecimal():
            res = res * 10 + int(x)
    print(res)

    cnt = 0
    for i in range(1,res+1):
        if res % i == 0 :
            cnt += 1
    print(cnt)