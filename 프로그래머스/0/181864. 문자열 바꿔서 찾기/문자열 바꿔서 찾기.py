def solution(myString, pat):
    new_str =''
    for i in myString:
        if i=='A':
            i='B'
        elif  i=='B':
            i='A'
        new_str+= i
    
    if pat in new_str:
        answer = 1
    else :
        answer = 0
    return answer