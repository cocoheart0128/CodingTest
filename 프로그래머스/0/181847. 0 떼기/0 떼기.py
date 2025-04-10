def solution(n_str):
    if n_str[0]=='0':
        i_list = []
        for i in range(len(n_str)):
            if n_str[i]!='0':
                i_list.append(i)
        print(i_list)
        answer = n_str[i_list[0]:]
    else :
        answer = n_str
        
            
    return answer