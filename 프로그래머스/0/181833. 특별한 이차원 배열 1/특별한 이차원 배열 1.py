def solution(n):
    answer = []
    for i in range(n):
        ind = [0]*n
        ind[i]=1
        answer.append(ind)
    return answer