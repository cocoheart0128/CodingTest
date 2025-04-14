def solution(n):
    matrix = [[0] * n for _ in range(n)]
    current = 1
    for layer in range((n + 1) // 2):
        start = layer
        end = n - layer - 1
        
        # 상단 행 (좌→우)
        for col in range(start, end + 1):
            matrix[start][col] = current
            current += 1
        
        # 우측 열 (상→하, 첫 요소 제외)
        for row in range(start + 1, end + 1):
            matrix[row][end] = current
            current += 1
        
        if start < end:
            # 하단 행 (우→좌, 첫 요소 제외)
            for col in range(end - 1, start - 1, -1):
                matrix[end][col] = current
                current += 1
            
            # 좌측 열 (하→상, 첫 요소 제외)
            for row in range(end - 1, start, -1):
                matrix[row][start] = current
                current += 1
    return matrix