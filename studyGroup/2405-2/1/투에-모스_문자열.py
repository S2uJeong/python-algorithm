"""
점화식
f(0) = 0
f(2n) = f(n)
f(2n+1) = 1 - f(n)
"""

k = int(input())

def recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n % 2:
        return 1- (recursive(n//2))
    else:
        return recursive(n//2)

# 메모리 초과
def fail(k):
    def swap(list):
        new_list = []
        for n in list:
            if n == 1 :
                new_list.append(0)
            else:
                new_list.append(1)
        return new_list

    s = [0]
    while True:
        if len(s) >= k:
            return s[k-1]
        new_list = swap(s)
        s.extend(new_list)

    return 0


#=== 결과 출력
print(fail(k))
print(recursive(k-1))