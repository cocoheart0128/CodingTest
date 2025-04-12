def solution(board, k):
    result=[]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i+j<=k:
                print(board[i][j])
                result.append(board[i][j])
    answer = sum(result)
    return answer