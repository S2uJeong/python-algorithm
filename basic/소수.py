print("[1 ~ 입력하는 값] 범위에서 소수의 개수를 계산하여 출력합니다.")
in_num = int(input())
def prime_cnt(p_num):
    cnt = 0
    prime_list = [0]*(p_num+1)
    for i in range(2,p_num +1):
        if prime_list[i] == 0 :
            cnt += 1
            for j in range(i, p_num+1, i):
                prime_list[j] = 1
    return cnt

print(prime_cnt(in_num))


# 소수인지 판별
def is_prime(num):
    if num < 2 :
        return False
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True