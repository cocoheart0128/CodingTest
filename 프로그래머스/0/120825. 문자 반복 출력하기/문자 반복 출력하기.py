def solution(my_string, n):
    answer = ''
    for i in my_string:
        i=i*n
        answer+=i
    return answer