import math
def solution(numer1, denom1, numer2, denom2):
    answer=[0,0]
    answer[1]=denom1*denom2
    answer[0]=numer1*denom2+numer2*denom1
    gcd = math.gcd(answer[0], answer[1])
    answer[1]=answer[1]/gcd
    answer[0]=answer[0]/gcd
        
        
    return answer