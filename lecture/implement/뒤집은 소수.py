# 숫자 뒤집는 함수
def reverse_int(p_num) :
    reversed_str = str(p_num)[::-1]
    result = int(reversed_str)
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

def first_try():
    print('공백을 기준으로 숫자들을 한 줄에 입력해주세요')
    nums = list(map(int,input().split()))
    result = []
    for num in nums :
        if is_prime(reverse_int(num)) :
            result.append(reverse_int(num))

    return result

print(first_try())

