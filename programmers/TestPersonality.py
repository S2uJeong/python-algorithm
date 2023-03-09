def solution(survey, choices):
    answer = ''
    RTCFJMAN = [0, 0, 0, 0, 0, 0, 0, 0]
    str = "RTCFJMAN"

    for i in enumerate(survey):
        RTCFJMAN[str.index(survey[i][1])] += choices[i] - 4

    if (RTCFJMAN[0] >= RTCFJMAN[1]):
        answer += "R"
    else:
        answer += "T"

    if (RTCFJMAN[2] >= RTCFJMAN[3]):
        answer += "C"
    else:
        answer += "F"

    if (RTCFJMAN[4] >= RTCFJMAN[5]):
        answer += "J"
    else:
        answer += "M"

    if (RTCFJMAN[6] >= RTCFJMAN[7]):
        answer += "A"
    else:
        answer += "N"

    return answer
