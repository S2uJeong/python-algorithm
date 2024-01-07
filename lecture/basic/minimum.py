def getMinimum(v_list):
    tmp = v_list[0]
    for num in v_list:
        if num < tmp:
            tmp = num
    return tmp

print(getMinimum([4,5,2,8,2,564,234]))