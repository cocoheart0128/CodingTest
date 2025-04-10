def solution(myString):
    str_l = myString.split('x')
    answer = [len(i) for i in str_l]
    return answer