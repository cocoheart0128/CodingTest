def solution(str_list):
    answer=[]
    if 'l'in str_list and 'r' in str_list:
        indl = str_list.index('l')
        indr = str_list.index('r')
        if indl<indr:
            answer = str_list[:indl]
        else:
            answer = str_list[indr+1:]
    elif 'l'in str_list:
        indl = str_list.index('l')
        answer = str_list[:indl]
    elif 'r'in str_list:
        indr = str_list.index('r')
        answer = str_list[indr+1:]
    else:
        answer = []
    return answer