signal = {'a': 'n', 'b': 'd', 'c': 'a', 'd': 'b', 'e': 'e', 'f': 'l', 'g': 'j', 'h': 'o', 'i': 'z', 'j': 'u', 'k': 'y',
          'l': 'v', 'm': 'w', 'n': 'q', 'o': 'x', 'p': 'r', 'q': 'p', 'r': 'f', 's': 'g', 't': 't', 'u': 'm', 'v': 'h',
          'w': 'i', 'x': 'c', 'y': 'k', 'z': 's'}


# signal을 해독해서 반환하는 함수를 작성해 주세요.
def code(code):
    answer = ''
    for i in range(len(code)):
        if code[i] in signal:
            answer += signal[code[i]]
        else:
            answer += code[i]

    return answer

print(code('w fhle khj'))
