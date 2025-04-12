def solution(names):
    answer=[]
    for i in range(len(names)):
        print(names[i])
        if i%5==0:
            answer.append(names[i])
    return answer