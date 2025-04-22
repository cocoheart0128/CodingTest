def solution(age):
    answer=''
    for s in str(age):
        a = chr(ord('a')+int(s))
        answer+=a
    return answer