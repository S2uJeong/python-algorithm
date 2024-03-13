# 소수인지 판별
def is_prime(num):
    if num == 1 :
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 :
            return False
    return True

# 1~10000까지의 소수 리스트를 생성
prime_list = []
for num in range(2,10001):
    if is_prime(num) :
        prime_list.append(num)

print(prime_list)
def goldbach(arr):
    result = []
    for a in arr :
        print(f'num = {a}')
        prime1, prime2 = cal(a, prime_list)
        result.append((prime1, prime2))
    result.sort()
    print(result)
    return result

def cal(num, prime_list):
    prime1 = prime2 = int(num/2)
    if prime1 in prime_list :
        return prime1, prime2
    else :
        while True :
            if prime1 in prime_list and prime2 in prime_list:
                break
            prime1 = prime1 - 1
            prime2 = num - prime1
    return prime1, prime2


arr = [int(x) for x in input().split()]

for i in goldbach(arr):
    print(i[0], i[1])
