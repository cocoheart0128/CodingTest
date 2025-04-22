def solution(n):
    matrix = [[0] * n for _ in range(n)]

    # 2. 방향 벡터 (→, ↓, ←, ↑)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir_idx = 0  # 현재 방향 인덱스

    x, y = 0, 0  # 시작 위치
    for num in range(1, n * n + 1):
        matrix[x][y] = num  # 현재 위치에 숫자 채우기

        # 다음 위치 계산
        dx, dy = directions[dir_idx]
        nx, ny = x + dx, y + dy

        # 다음 위치가 범위를 벗어나거나 이미 채워진 경우 방향 전환
        if not (0 <= nx < n and 0 <= ny < n) or matrix[nx][ny] != 0:
            dir_idx = (dir_idx + 1) % 4  # 방향 전환
            dx, dy = directions[dir_idx]
            nx, ny = x + dx, y + dy

        # 다음 위치로 이동
        x, y = nx, ny
    return matrix