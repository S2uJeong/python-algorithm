N = int(input())

# 소수인지 판별하는 함수
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def dfs(n):
    if len(str(n)) == N:
        print(n)
        return
    for i in range(10):
        # nb = int(str(n) + str(i))
        nb = n*10 + i
        if is_prime(nb):
            dfs(nb)
        else:
            continue

first_prime = [2,3,5,7]
for i in first_prime:
    dfs(i)
