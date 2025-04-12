def solution(arr, flag):
    answer = []
    n = len(flag)
    for i in range(n):
        print(i)
        if flag[i] is True:
            answer=answer+[arr[i]]*arr[i]*2
            # print(answer)
        elif flag[i] is False:
            answer = answer[:-arr[i]]
            # print(answer)
    return answer