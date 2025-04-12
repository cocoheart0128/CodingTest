def solution(n, slicer, num_list):
    if n == 1:
        answer = num_list[0:slicer[1]+1]
    elif n==2:
        answer = num_list[slicer[0]:]
    elif n==3:
        answer = num_list[slicer[0]:slicer[1]+1]
    elif n==4:
        mid = num_list[slicer[0]:slicer[1]+1]
        cnt = 0
        answer = []
        for i in range(len(mid)):
            cnt += 1
            if cnt%(slicer[2])!=0:
                answer.append(mid[i])
    else:
        pass
    
    return answer