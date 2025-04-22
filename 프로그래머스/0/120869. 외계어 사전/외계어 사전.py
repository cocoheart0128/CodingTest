def solution(spell, dic):
    la = []
    spell = ''.join(sorted(spell))
    for word in dic:
        l = [s for s in word]
        ls=''.join(sorted(l))
        la.append(ls)
    print(l)
    if spell in la:
        answer = 1
    else:
        answer=2
    return answer