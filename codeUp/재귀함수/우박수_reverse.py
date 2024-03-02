"""
https://codeup.kr/problem.php?id=1928
"""

def recur(num) :

    if num == 1 :
        print(1)
        return

    if num % 2 == 0 :
        recur(num/2)
    else :
        recur(3*num+1)

    print(int(num))


recur(int(input()))