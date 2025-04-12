def solution(a, b):
    lena=len(str(a))
    lenb=len(str(b))

    an=int('1'+'0'*lenb)
    bn=int('1'+'0'*lena)
    
    sumab=a*an+b
    sumba=2*a*b
    
    if sumab>sumba:
        return sumab
    else:
        return sumba
    