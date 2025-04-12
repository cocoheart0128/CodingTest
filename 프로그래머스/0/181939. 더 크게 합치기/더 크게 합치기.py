def solution(a, b):
    sum_len=len(str(a))+len(str(b))
    lena=sum_len-len(str(a))
    fixa=int('1'+'0'*lena)
    lenb=sum_len-len(str(b))
    fixb=int('1'+'0'*lenb)
    
    if a*fixa+b>b*fixb+a:
        return a*fixa+b
    else:
        return b*fixb+a
    
    return answer