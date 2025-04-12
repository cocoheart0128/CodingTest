def solution(arr):
    num_list = []
    for i in range(len(arr)):
        if arr[i]==2:
            num_list.append(i)
    
    if len(num_list)>1:
        answer = arr[num_list[0]:num_list[-1]+1]
    elif len(num_list)==1:
        answer = arr[num_list[0]:num_list[0]+1]
    else:
        answer = [-1] 
    return answer