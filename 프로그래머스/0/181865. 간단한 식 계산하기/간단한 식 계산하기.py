def solution(binomial):
    if '+' in binomial:
        op = '+'
        a = binomial.split(op)[0]
        b = binomial.split(op)[1]
        answer = int(a)+int(b)
    elif '-' in binomial:
        op = '-'
        a = binomial.split(op)[0]
        b = binomial.split(op)[1]
        answer = int(a)-int(b)
    elif '*' in binomial:
        op = '*'
        a = binomial.split(op)[0]
        b = binomial.split(op)[1]
        answer = int(a)*int(b)
    return answer