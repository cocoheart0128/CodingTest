def solution(start_num, end_num):
    answer = []
    cnt=start_num-end_num+1
    for i in range(cnt):
        num=start_num-i
        answer.append(num)

    return answer