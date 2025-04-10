def solution(num_list):
    answer=0
    summ=0
    ku=1
    for i in num_list:
        summ+=i
        ku*=i
        
    if len(num_list)>=11:
        answer = summ
    else:
        answer = ku
    return answer