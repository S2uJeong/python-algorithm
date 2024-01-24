def binary(num) :
    if num == 0 :
        return '0'
    elif num == 1 :
        return '1'

    if(num%2 == 0):
        return binary(num//2) + '0'
    else :
        return binary(num//2) + '1'


num = int(input())
print(binary(num))