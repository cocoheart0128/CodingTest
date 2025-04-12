def solution(str_list, ex):
    answer = ''.join([str for str in str_list if ex not in str])
    return answer