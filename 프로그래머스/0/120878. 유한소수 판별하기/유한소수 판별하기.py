import math
def solution(a, b):
    gcd=math.gcd(a,b)
    gcd_a=a//gcd
    gcd_b=b//gcd
    # 2와 5를 제거
    while gcd_b % 2 == 0:
        gcd_b //= 2
    while gcd_b % 5 == 0:
        gcd_b //= 5
    return 1 if gcd_b == 1 else 2