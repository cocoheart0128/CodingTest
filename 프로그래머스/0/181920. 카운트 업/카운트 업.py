def solution(start_num, end_num):
    answer = [start_num]
    
    while start_num<end_num:
        start_num +=1
        answer.append(start_num)
     
    return answer