def solution(num_list):
    a = (sum(num_list))**2
    b=1
    for i in num_list:
        b=b*i
    if a>b:
        answer=1
    elif a<b:
        answer=0
    return answer