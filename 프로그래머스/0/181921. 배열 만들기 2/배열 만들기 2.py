def solution(l, r):
    answer = []
    lst = list(range(0, 10))
    lst.remove(0)
    lst.remove(5)
    lst = [str(n) for n in lst]

    for i in range(l,r+1):
        if i%5==0:
            if not any(item in str(i) for item in lst):
                answer.append(i)
    
    if len(answer) == 0:
        answer = [-1]
            
    
                    
    print(answer)                
    return answer