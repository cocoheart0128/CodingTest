def solution(numLog):
    answer=[]
    for i in range(0,len(numLog)-1):
        val = numLog[i+1]-numLog[i]
        if val == 1:
            answer.append('w')
        elif val == -1:
            answer.append('s')
        elif val == 10:
            answer.append('d')
        elif val == -10:
            answer.append('a')
    answer=''.join(answer)
    return answer