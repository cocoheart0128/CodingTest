def solution(n):
    answer = [n]
    
    while n!=1:
        if n%2==0:
            n=n/2
        elif n%2!=0:
            n=n*3+1
        answer.append(n)
    return answer