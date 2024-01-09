# 숫자 뒤집는 함수
def reverse_int(p_num) :
    reversed_str = str(p_num)[::-1]
    result = int(reversed_str)
    return result

def reverse_int_example(p_num):
    result = 0
    while p_num > 0 :
        tmp = p_num % 10
        result = result * 10 + tmp
        p_num //= 10
    return result


# 소수인지 확인하는 함수
def is_prime(p_num):
   cd_list = []
   for i in range(2,p_num): # 1과 자기자신을 제외한 부분만 나눈다.
       if p_num % i == 0 :
           cd_list.append(i)
   if cd_list :
      return False
   else :
      return True

def is_prime_example(p_num):
    if p_num == 1 :
        return False
    for i in range(2,p_num//2+1): # 반절까지만 탐색해도 결과는 똑같으므로, 또한 자기 자신의 수까지 가지 않게 함으로써 아래 조건식이 성립됨.
        if p_num % i == 0 :
            return False
        else :
            return True

def first_try():
    print('공백을 기준으로 숫자들을 한 줄에 입력해주세요')
    nums = list(map(int,input().split()))
    result = []
    for num in nums :
        if is_prime(reverse_int(num)) :
            result.append(reverse_int(num))

    return result

print(first_try())
