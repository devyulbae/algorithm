def solution(x, y, d, board):  
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    board[x][y] = 2  #청소한 칸은 2로 변경한다.
    clean_cnt = 1

    while True:
        if board[x][y]==0:
            board[x][y] = 2
            clean_cnt += 1
        
        all_cleaned = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                all_cleaned = False
                break
        if all_cleaned:
            back_d = (d + 2) % 4
            back_x, back_y = x + dx[back_d], y + dy[back_d]
            if not (0 <= back_x < n and 0 <= back_y < m and board[back_x][back_y] != 1):
                return clean_cnt
            else:
                x, y = back_x, back_y
        elif not all_cleaned:
            d = (d + 3) % 4
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                x, y = nx, ny

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
print(solution(r, c, d, arr))