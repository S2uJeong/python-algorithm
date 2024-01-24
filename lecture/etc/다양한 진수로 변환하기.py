def trans(base, num):
    num_ch = ['0','1','2','3','4','5','6','7','8','9']
    num_ch += ['A','B','C','D','E','F']

    if num < base :
        print(num_ch[num],end='')
    else:
        trans(base,num//base)
        print(num_ch[num%base],end ='')

num = int(input())

trans(2,num)





