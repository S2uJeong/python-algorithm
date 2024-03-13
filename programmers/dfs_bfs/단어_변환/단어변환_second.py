from collections import deque
def solution(begin, target, words):
    dQ = deque()
    dQ.append((begin, 0))# (word, step)
    while dQ :
        word, step = dQ.popleft()
        if word == target :
            return step
        else :
            for w in words:
                cnt = 0
                for j in range(len(w)):
                    if w[j] != word[j]:
                        cnt += 1
                if cnt == 1 :
                    dQ.append((w,step+1))

    return 0

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))