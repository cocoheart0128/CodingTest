def solution(my_string):
    f_answer = my_string.split(' ')
    answer=[]
    for i in f_answer:
        if len(i)!=0:
            answer.append(i)
            
    return answer