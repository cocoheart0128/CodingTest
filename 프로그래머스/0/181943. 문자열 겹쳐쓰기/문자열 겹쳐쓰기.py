def solution(my_string, overwrite_string, s):
    l = len(overwrite_string)
    answer=my_string[0:s]+overwrite_string+my_string[s+l:]
    return answer