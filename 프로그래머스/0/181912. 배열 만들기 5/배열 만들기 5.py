def solution(intStrs, k, s, l):
    result = []
    
    for str in intStrs:
        # 부분 문자열을 잘라내고 정수로 변환
        i = int(str[s:s+l])
        
        # 조건을 만족하면 결과 리스트에 추가
        if i > k:
            result.append(i)
    
    return result