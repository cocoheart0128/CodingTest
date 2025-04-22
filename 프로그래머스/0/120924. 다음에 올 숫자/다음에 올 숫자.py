def solution(common):
    ll=[]
    answer = 0
    for i in range(len(common)-1):
        if common[i+1]-common[i]==common[i+2]-common[i+1]:
            print(common[i+2]-common[i+1])
            answer = common[-1]+(common[i+1]-common[i])
        else:
            answer = common[-1]*(common[i+1]/common[i])
        break
    return answer