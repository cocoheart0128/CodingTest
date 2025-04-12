def solution(num_list):
    sum_j=sum_h=0
    for i in range(len(num_list)):
        if i%2==0:
            sum_j+=num_list[i]
        elif i%2!=0:
            sum_h+=num_list[i]
    
    if sum_j>=sum_h:
        answer = sum_j
    else: 
        answer = sum_h
    return answer