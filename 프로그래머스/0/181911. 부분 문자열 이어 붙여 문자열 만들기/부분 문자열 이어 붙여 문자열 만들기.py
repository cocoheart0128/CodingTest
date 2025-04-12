def solution(my_strings, parts):
    answer=''
    for i in range(len(my_strings)):
        str = my_strings[i]
        idx = parts[i]
        answer+=str[idx[0]:idx[1]+1]
    return answer