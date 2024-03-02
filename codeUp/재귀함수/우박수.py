"""
https://codeup.kr/problem.php?id=1928
"""

def recur(num) :
    print(int(num))

    if num == 1 :
        return

    if num % 2 == 0 :
        return recur(num/2)
    else :
        return recur(3*num+1)


recur(int(input()))