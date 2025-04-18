def solution(my_string):
    l = [i for i in my_string]
    answer = ''.join (l[::-1])
    return answer