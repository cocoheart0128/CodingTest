def solution(id_pw, db):
    id=[]
    pw=[]
    for i in db:
        id.append(i[0])
        pw.append(i[1])
    
    if id_pw[0] in id:
        ind = id.index(id_pw[0])
        if pw[ind]==id_pw[1]:
            answer='login'
        else:
            answer='wrong pw'
    else:
        answer='fail'
    return answer