def solution(n, k):
    s = int(n/10)
    answer = n*12000+k*2000-2000*s
    return answer