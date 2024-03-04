"""
https://school.programmers.co.kr/learn/courses/30/lessons/72410
제거를 어떻게 표현해야 할까를 고민함.
- 문자열이라고 할 떄,   '' 이면 아예 없어지나?
- 만약 공백으로 여백이 생기면 strip 해줘야겠다.

왜 틀렸는지 하나씩 분석할것,,
"""
new_id = "...!@BaT#*..y.abcdefghijklm"
def solution(new_id):
    id = checkLength(fillA(removeDot(removeExtendDot(removeSymbols(bigToSmall(new_id))))))

    return id
def bigToSmall(new_id) :
    new_id.lower()
    return new_id

def removeSymbols(new_id):
    for i in range(len(new_id)) :
        if new_id[i] in "~!@#$%^&*()=+[{]}:?,<>/":
            new_id.replace(new_id[i],'')
    return new_id

def removeExtendDot(new_id):
    for i in range(len(new_id)):
        for j in range(i,len(new_id)):
            if new_id[i] == '.' and new_id[j] == '.':
                print(str(i) +"_" + str(j) + ":" + new_id[i], new_id[j] + str("bool" + new_id[i] == '.' and new_id[j] == '.'))
                new_id.replace(new_id[i],'')

    return new_id

def removeDot(new_id):
    if new_id[0] == '.' :
       new_id.replace(new_id[0], '')
    if new_id[-1] == '.' :
        new_id.replace(new_id[-1], '')
    return new_id

def fillA(new_id):
    if len(new_id) == 0 :
        new_id = 'a'
    return new_id

def checkLength(new_id) :
    if len(new_id) >= 16 :
        new_id = new_id[0:16]
        if new_id[-1] == '.':
            new_id.replace(new_id[-1], '')

    if len(new_id) <= 2 :
        new_id = new_id[0:(len(new_id)+1)]
        while len(new_id) < 3 :
            new_id = new_id + new_id[-1]

    return new_id


print(solution(new_id))