def solution(arr):
    answer = []
    for i in arr:
        i_arr=[i]*i
        for j in i_arr:
            answer.append(j)
    return answer