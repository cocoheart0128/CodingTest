def solution(n):
    l = [i**2 for i in range(int(n/2))]
    if n in l:
        answer = 1
    else:
        answer = 2
    return answer