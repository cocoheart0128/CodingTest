def function(num):
    re = 1
    for i in range(1,num+1):
        re=re*i
    return re
        
def solution(balls, share):
    answer = function(balls)/(function(balls-share)*function(share))
    return answer